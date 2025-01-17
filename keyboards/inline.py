from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.callback import all_stat

select_stat = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Статистика за сегодня',
            callback_data='today_statistic'
        )
    ],
    [
        InlineKeyboardButton(
            text='Статистика за неделю',
            callback_data='weekly_statistic'
        )
    ],
    [
        InlineKeyboardButton(
            text='Статистика за месяц',
            callback_data='monthly_statistic'
        )
    ],
    [
        InlineKeyboardButton(
            text='Статистика за все время',
            callback_data='all_statistic'
        )
    ]
])