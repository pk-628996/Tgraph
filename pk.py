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
START_TEXT=""" Hi, This is for testing {} """
ABOUT_TEXT="""This is about text """

@Pk.on_message(filters.private & filters.command("start"))
async def start(pk, update):
     
    await update.reply_text(
     text=START_TEXT.format(update.from_user.mention),
     reply_markup=START_BUTTON
    )
@Pk.on_message(filters.private & filters.command("id"))
async def id(pk, message):
 
   await message.reply_text(
    text=f""" here is your chat id ` {message.from_user.id} `"""
   )




@Pk.on_callback_query()
async def cb_data(bot, update):
    if update.data == 'about':
       await update.message.edit_text(
           text=ABOUT_TEXT,
           disable_web_page_preview=True
       ),
    elif update.data == 'menu':
       await update.message.reply_message(
          reply_markup=MENU_BUTTON,
          disable_web_page_preview=True
       ),
    elif update.data == 'close':
       await update.message.reply_message(
          text="""closed""",
          disable_web_page_preview=True
       ),    
    else:
        await update.message.delete()

Pk.run()

         


     

    
