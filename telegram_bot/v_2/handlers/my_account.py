from aiogram.types import CallbackQuery
from keyboards.inline import get_inline_keyboard
from aiogram.types import Message


async def my_account(message: Message) -> None:
    """
    Обрабатываем настройки
    """
    await message.answer(text='Настройки', reply_markup=get_inline_keyboard())
    await message.delete()
