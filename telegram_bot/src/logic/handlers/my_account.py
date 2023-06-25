from aiogram.types import CallbackQuery, Message
from keyboards.inline import get_inline_keyboard
from utils.callbackdata import MyAccountCallBackData
from aiogram import Router, F
from aiogram.filters import Text


account_info_router = Router(name="info")


@account_info_router.message(Text(text=['Настройки']))
async def my_account(message: Message) -> None:
    """
    Обрабатываем настройки
    """
    await message.answer(text='Настройки', reply_markup=get_inline_keyboard())
    await message.delete()


@account_info_router.message(MyAccountCallBackData.filter(F.action == 'balance'))
async def balance(call: CallbackQuery, callback_data: MyAccountCallBackData):
    text = f'Ваш баланс равен "из базы данных"'
    await call.answer(text)


@account_info_router.message(MyAccountCallBackData.filter(F.action == 'statistics'))
async def statistics(call: CallbackQuery, callback_data: MyAccountCallBackData):
    text = f'Здесь будет выводиться история ваших заказов'
    await call.answer(text)


@account_info_router.message(MyAccountCallBackData.filter(F.action == 'price'))
async def price(call: CallbackQuery, callback_data: MyAccountCallBackData):
    text = f'Здесь будет выведена цена из базы'
    await call.answer(text)
