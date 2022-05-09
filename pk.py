import os 
from BUTTONS import START_BUTTON, MENU_BUTTON
from pyrogram import Client, filters
from telegraph import upload_file
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Pk = Client(
      "Telegraph Uploader Bot",
      bot_token=os.environ.get("BOT_TOKEN"),
      api_id=os.environ.get("API_ID"),
      api_hash=os.environ.get("API_HASH")
)
DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")

START_TEXT=""" Hi, This is for testing {} """
ABOUT_TEXT="""This is about text """


@Pk.on_message(filters.private & filters.command("start"))
async def start(pk, update):
     
    await update.reply_text(
     text=START_TEXT.format(update.from_user.mention),
     reply_markup=START_BUTTON
    )
@Pk.on_message(filters.private & filters.command("cmds"))
async def cmds(pk, cmds):
   await cmds.reply_text(
    text= """ Available Commands \n
          /start -start the bot \n
          /id - show your chat id \n
          /cmds - list available commands"""
   )

@Pk.on_message(filters.private & filters.command("id"))
async def id(pk, message):
 
   await message.reply_text(
    text=f""" here is your chat id ` {message.from_user.id} `"""
   )
@Pk.on_message(filters.private & filters.media)
async def getmedia(pk, update):  
   medianame = DOWNLOAD_LOCATION + str(update.from_user.id)
   try:
      message = await update.reply_text(
       text="Downloading...",
       quote=True,
       disable_web_page_preview=True
      )
      await pk.download_media(
       message=update,
       file_name=medianame
      )
      response = upload_file(medianame)
      try: 
           os.remove(medianame)
      except:
          pass
   except Exception as error:
        text=f"Error :- <code>{error}</code>"
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton('More Help', callback_data='help')]]
        )
        await message.edit_text(
            text=text,
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )
        return
        text=f"**Link :-** `https://telegra.ph{response[0]}`"
        reply_markup=InlineKeyboardMarkup(
            [
               [
                   InlineKeyboardButton(text="Open Link", url=f"https://telegra.ph{response[0]}"),
                   InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
               ]
           ]
        )
        await message.edit_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
        )
@Pk.on_callback_query()
async def cb_data(bot, update):
    if update.data == 'about':
       await update.message.edit_text(
           text=ABOUT_TEXT,
           reply_markup=MENU_BUTTON,
           disable_web_page_preview=True
       ),
    elif update.data == 'menu':
       await update.message.edit_text(
          text="menu",
          reply_markup=MENU_BUTTON,
          disable_web_page_preview=True
       ),
    elif update.data == 'help':
      await update.message.edit_text(
        text="This is help text",
        reply_markup=MENU_BUTTON,
        disable_web_page_preview=True
      ),
    elif update.data == 'close':
       await update.message.edit_text(
          text="""closed""",
          disable_web_page_preview=True
       ),    
    else:
        await update.message.delete()

Pk.run()

         


     

    
