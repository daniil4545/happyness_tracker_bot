import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers.basic import get_start
from settings import settings


async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот запущен.')
    
async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен.')


async def start():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=settings.bots.bot_token)
    dp = Dispatcher()

    dp.message.register(get_start)

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close(bot)

if __name__ == "__main__":
    asyncio.run(start())