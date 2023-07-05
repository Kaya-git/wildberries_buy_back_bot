from aiogram.types import CallbackQuery, Message
from ..keyboards.inline import get_inline_keyboard
from utils.callbackdata import AccountInfo
from aiogram import Router, F
from aiogram.filters import Text
from database import Database
from middlewares import DatabaseMiddleware
from database.models import User


account_info_router = Router(name="info_menu")
account_info_router.callback_query.middleware(DatabaseMiddleware())

@account_info_router.message(Text(text=['Настройки']))
async def my_account(message: Message) -> None:
    """
    Обрабатываем настройки
    """
    await message.answer(text='Настройки', reply_markup=get_inline_keyboard())
    await message.delete()


@account_info_router.callback_query(AccountInfo.filter(F.action == 'balance'))
async def balance(call: CallbackQuery, callback_data: AccountInfo, db: Database):
    user_id = call.from_user.id
    stmt = await db.user.get_by_where(User.user_id==user_id)
    for x in stmt:
        print(x.user_id)
        print(x.user_name)
        print(x.balance)
    text = f'Ваш баланс равен'
    await call.answer(text)


@account_info_router.callback_query(AccountInfo.filter(F.action == 'statistics'))
async def statistics(call: CallbackQuery, callback_data: AccountInfo):
    text = f'Здесь будет выводиться история ваших заказов'
    await call.answer(text)


@account_info_router.callback_query(AccountInfo.filter(F.action == 'price'))
async def price(call: CallbackQuery, callback_data: AccountInfo):
    text = f'Здесь будет выведена цена из базы'
    await call.answer(text)
