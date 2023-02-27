from aiogram.types import Message
from keyboards.inline import my_account, get_inline_keyboard
from keyboards.reply import kb_main_menu

async def start(message: Message) -> None:
    """
    Хендлер на команду старта
    """
    await message.answer('Главное меню', reply_markup=kb_main_menu)
    await message.delete()


async def my_account(message: Message) -> None:
    """
    Обрабатываем настройки
    """
    await message.answer(text='Настройки', reply_markup=get_inline_keyboard())
    await message.delete()
