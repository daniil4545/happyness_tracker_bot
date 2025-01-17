from aiogram import Bot
from aiogram.types import Message
from database.database import save_message

async def get_start(message: Message, bot: Bot):
    await message.answer(f'''Привет, {message.from_user.first_name}! Рад тебя видеть :)
Я - трекер счастья, создан чтобы помочь тебе записывать моменты радости и счастья в твоей жизни.
Просто напиши, почему ты чувствуешь себя счастливым сейчас, и я сохраню это для тебя.''')

async def get_happiness(message: Message, bot: Bot):
    try: 
        save_message(message.from_user.id, message.text)
        await message.answer("Событие записано! Ты только что стал немного счастливее 🌟")
    except:
        await message.answer("Что-то пошло не так...")