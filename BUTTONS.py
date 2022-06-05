from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




START_BUTTON = InlineKeyboardMarkup(
    [
      [
        InlineKeyboardButton('Menu🔖', callback_data='menu')
      ]
    ]
)
MENU_BUTTON = InlineKeyboardMarkup(
    [
      [
         InlineKeyboardButton('About📃', callback_data='about'),
         InlineKeyboardButton('Help⁉️', callback_data='help')
      ],
      [
         InlineKeyboardButton('<---', callback_data='menu'),
         InlineKeyboardButton('close❌', callback_data='close')
      ]
    ]
)
