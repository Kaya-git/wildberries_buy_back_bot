from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_keyboard():
    inline_keyboard_builder = InlineKeyboardBuilder()
    inline_keyboard_builder.button(text='Мой баланс', callback_data='balance')
    inline_keyboard_builder.button(text='Статистика', callback_data='statistics')
    inline_keyboard_builder.button(text='Задать вопрос', callback_data='ask_question')
    inline_keyboard_builder.button(text='Прайслист', callback_data='prices')

    inline_keyboard_builder.adjust(2,2)
    return inline_keyboard_builder.as_markup()