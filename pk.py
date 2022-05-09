import os 
from pyrogram import Client, filters
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
     reply_markup= InlineKeyboardMarkup(
         [
           [ 
               InlineKeyboardButton('about' , callback_data='about')
           ]
         ]
     )
    )
@Pk.on_message(filters.private & filters.command("id"))
async def id(pk, send):
 
   await send.reply_text(
    text='here is your id' + command.chat_id
   )




@Pk.on_callback_query()
async def cb_data(bot, update):
    if update.data == 'about':
       await update.message.edit_text(
           text=ABOUT_TEXT
       )
    else:
        await update.message.delete()

Pk.run()

         


     

    
