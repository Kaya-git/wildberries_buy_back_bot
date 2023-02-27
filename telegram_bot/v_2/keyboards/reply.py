from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Самовыкуп')
        ],
        [
            KeyboardButton(text='Рефералка'),
            KeyboardButton(text='Настройки')
        ]
    ],
    resize_keyboard=True
)


cancel_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отмена')
        ]
    ],
    resize_keyboard=True
)
