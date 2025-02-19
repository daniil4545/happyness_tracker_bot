import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram import F
from aiogram.filters import Command
from handlers.basic import get_start, get_happiness, get_statistic
from handlers.callback import all_stat, today_stat, weekly_stat, monthly_stat
from utils.commands import set_commands
from settings import settings


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен.')
    
async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен.')


async def start():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=settings.bots.bot_token)
    dp = Dispatcher()

    dp.message.register(get_start, Command('start'))

    dp.message.register(get_statistic, F.text == 'Посмотреть статистику')
    dp.callback_query.register(all_stat, F.data.startswith('all_'))
    dp.callback_query.register(today_stat, F.data.startswith('today_'))
    dp.callback_query.register(weekly_stat, F.data.startswith('weekly_'))
    dp.callback_query.register(monthly_stat, F.data.startswith('monthly_'))

    dp.message.register(get_happiness)

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close(bot)

if __name__ == "__main__":
    asyncio.run(start())