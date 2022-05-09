import os 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Pk = Client(
      "Telegraph Uploader Bot",
      bottoken=os.environ.get("BOT_TOKEN"),
      apiid=os.environ.get("API_ID"),
      apihash=os.environ.get("API_HASH")
)
START_TEXT=""" Hi, This is for testing {} """

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



@Pk.on_callback_query()
async def cb_data(bot, update):
    if update.data == 'about':
       await update.message.edit_text(
           text=START_TEXT.format(update.from_user.mention)
       )
    else:
        await update.message.delete()

Pk.run()

         


     

    
