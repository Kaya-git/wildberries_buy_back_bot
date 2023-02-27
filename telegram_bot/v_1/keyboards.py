from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


cb = CallbackData('ikb', 'action')


kb_main = ReplyKeyboardMarkup(
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


kb_acount = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Мой баланс', callback_data=cb.new('balance')),
            InlineKeyboardButton(text='Статистика', callback_data=cb.new('statistics'))
        ],
        [
            InlineKeyboardButton(text='Задать вопрос', callback_data=cb.new('ask_question'))
        ],
        [
            InlineKeyboardButton(text='Прайслист', callback_data=cb.new('prices'))
        ]
    ],
)


cancel_button = ReplyKeyboardMarkup(
    keyboard=[
    [KeyboardButton(text='Отмена')]
    ],
    resize_keyboard=True
)