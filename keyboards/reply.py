from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Посмотреть статистику')
    ]
], resize_keyboard=True, one_time_keyboard=True)