from aiogram.types import Message

from ..keyboards.reply import kb_main_menu
from aiogram.filters import Text
from aiogram import Router


referals_router = Router(name="referals")


@referals_router.message(Text(text=['Рефералка']))
async def share(message: Message) -> None:
    """
    Обрабатываем команду пригласить друга
    """

    await message.answer(
        text='В дальнейшем стоит добавить реферальную ссылку и добавлять на баланс деньги,'
        'если пользователь которого добавили, пополнит баланс',
        reply_markup=kb_main_menu
    )
