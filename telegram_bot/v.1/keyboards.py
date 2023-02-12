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


cb_balance = CallbackData('balance')
cb_statics = CallbackData('s_word', 'shop_pic', 'bb_quantity', 'spend_sum_in_rub')
cb_prices = CallbackData('service', 'price')
cb_ask = CallbackData('question')

keyboard_my_ac = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Мой баланс', callback_data='balance'),
            InlineKeyboardButton(text='Статистика', callback_data='s_word:shop_pic:bb_quantity:spend_sum')
        ],
        [
            InlineKeyboardButton(text='Задать вопрос', callback_data='service:price')
        ],
        [
            InlineKeyboardButton(text='Прайслист', callback_data='question')
        ]
    ],
)
