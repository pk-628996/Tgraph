import os 
from BUTTONS import START_BUTTON, MENU_BUTTON
from pyrogram import Client, filters
from telegraph import Telegraph , upload_file
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
@Pk.on_message(filters.photo)
async def uploadphoto(client, message):
   userid = str(message.chat.id)
   medianame= (f"./DOWNLOADS/{userid}.jpg")
   medianame = await client.download_media(
                  message="message", 
                  file_name = medianame)
   await message.reply_text('Down')
   try:
       tlink = Telegraph.upload_file(medianame)
       await message.edit_text(f"https://telegra.ph{tlink[0]}")
       os.remove(medianame)
   except:
       await message.edit_text("Something went wrong") 

@Pk.on_message(filters.animation)
async def uploadgif(client, message):
  if(message.animation.file_size < 5242880):
    message = await message.reply_text("Trying to Download")
    userid = str(message.chat.id)
    gif_path = (f"./DOWNLOADS/{userid}.mp4")
    gif_path = await client.download_media(message=message, file_name=gif_path)
    await message.edit_text("Trying to Upload...")
    try:
      tlink = upload_file(gif_path)
      await message.edit_text(f"https://telegra.ph{tlink[0]}")   
      os.remove(gif_path)   
    except:
      await message.edit_text("Something really Happend Wrong...") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb")

@Pk.on_message(filters.video)
async def uploadvid(client, message):
  if(message.video.file_size < 5242880):
    message = await message.reply_text("Trying to Download...")
    userid = str(message.chat.id)
    vid_path = (f"./DOWNLOADS/{userid}.mp4")
    vid_path = await client.download_media(message=message, file_name=vid_path)
    await message.edit_text("`Trying to Upload...")
    try:
      tlink = upload_file(vid_path)
      await message.edit_text(f"https://telegra.ph{tlink[0]}")     
      os.remove(vid_path)   
    except:
      await message.edit_text("Something really Happend Wrong...") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb")
@Pk.on_callback_query()
async def cb_data(bot, update):
    if update.data == 'about':
       await update.message.edit_text(
           text=ABOUT_TEXT,
           reply_markup=START_BUTTON,
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
        reply_markup=START_BUTTON,
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

         


     

    
