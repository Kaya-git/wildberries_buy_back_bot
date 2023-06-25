from aiogram.types import Message
from keyboards.reply import kb_main_menu
from aiogram import Router
from aiogram.filters import Command

start_router = Router(name="start")

@start_router.message(Command(commands=['start']))
async def start(message: Message) -> None:
    """
    Хендлер на команду старта
    """
    await message.answer('Главное меню', reply_markup=kb_main_menu)
    await message.delete()
