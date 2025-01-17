from aiogram import Bot
from aiogram.types import CallbackQuery
import database.database as db

async def all_stat(call:CallbackQuery, bot:Bot):
    user_id = call.message.chat.id
    num = db.get_total_count(user_id)
    answer = f'У тебя {num} счастливых событий за все время! Да ты счастливчик :)'
    await call.message.answer(answer)
    await call.answer()

async def today_stat(call:CallbackQuery, bot:Bot):
    user_id = call.message.chat.id
    num = db.get_today_count(user_id)
    answer = f'У тебя {num} счастливых событий за сегодня, отлично!'
    await call.message.answer(answer)
    await call.answer()

async def weekly_stat(call:CallbackQuery, bot:Bot):
    user_id = call.message.chat.id
    sum_week = db.get_weekly_count(user_id)
    happiest_day = db.get_happiest_day_in_week(user_id)
    average_daily_count = db.get_average_daily_count_week(user_id)
    answer = f'У тебя {sum_week} счастливых событий за неделю, а самый крутой день - {happiest_day}. В среднем, у тебя {average_daily_count} счастливых событий.'
    await call.message.answer(answer)
    await call.answer()

async def monthly_stat(call:CallbackQuery, bot:Bot):
    user_id = call.message.chat.id
    sum_month = db.get_monthly_count(user_id)
    happiest_day = db.get_happiest_day_in_month(user_id)
    average_daily_count = db.get_average_daily_count_month(user_id)
    answer = f'У тебя {sum_month} счастливых событий за месяц, а самый крутой день - {happiest_day}. В среднем, у тебя {average_daily_count} счастливых событий.'
    await call.message.answer(answer)
    await call.answer()