from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.callbackdata import MyAccountCallBackData


def get_inline_keyboard():
    inline_keyboard_builder = InlineKeyboardBuilder()
    inline_keyboard_builder.button(
        text='Мой баланс',
        callback_data=MyAccountCallBackData(
            action='balance'
        )
    )
    inline_keyboard_builder.button(
        text='Статистика',
        callback_data=MyAccountCallBackData(
            action='statistics'
        )
    )
    inline_keyboard_builder.button(
        text='Прайслист',
        callback_data=MyAccountCallBackData(
            action='price' 
        )
    )

    inline_keyboard_builder.adjust(2,1)
    return inline_keyboard_builder.as_markup()