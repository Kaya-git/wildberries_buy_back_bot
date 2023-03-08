from aiogram.types import Message
from keyboards.reply import kb_main_menu, cancel_button


async def start_buy_back(message: Message) -> None:
    """
    Обрабатываем команду сбора и информации для самовыкупа, ожидаем ввод ключевого слова от пользователя
    """
    await message.answer(
        text='Отправте в чат ключевое слово, по которому вы хотите продвинуться.'
        'Обязательно убедитесь в корректности орфографии',
        reply_markup=cancel_button
    )


async def cancel(message: Message):
    await message.answer(
        text='Отмена',
        reply_markup=kb_main_menu
    )
    await message.delete()
