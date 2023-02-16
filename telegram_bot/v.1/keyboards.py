from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


keyboard_main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Самовыкуп')
        ],
        [
            KeyboardButton(text='Поделиться'),
            KeyboardButton(text='Настройки')
        ]
    ],
    resize_keyboard=True
)


keyboard_my_ac = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Мой баланс', callback_data='balance'),
            InlineKeyboardButton(text='Статистика', callback_data='statistics')
        ],
        [
            InlineKeyboardButton(text='Задать вопрос', callback_data='ask_question')
        ],
        [
            InlineKeyboardButton(text='Прайслист', callback_data='prices')
        ]
    ],
)


keyboard_buy_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Указать сумму самовыкупа')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)