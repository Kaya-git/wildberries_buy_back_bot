from aiogram.types import Message
from keyboards.reply import kb_main_menu

async def start(message: Message) -> None:
    """
    Хендлер на команду старта
    """
    await message.answer('Главное меню', reply_markup=kb_main_menu)
    await message.delete()
