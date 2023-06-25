# from utils.callbackdata import MyAccountCallBackData
# from aiogram.types import CallbackQuery
# from aiogram import Router, F

# account_info_router = Router(name="info")

# @account_info_router.message(MyAccountCallBackData.filter(F.action == 'balance'))
# async def balance(call: CallbackQuery, callback_data: MyAccountCallBackData):
#     text = f'Ваш баланс равен "из базы данных"'
#     await call.answer(text)

# @account_info_router.message(MyAccountCallBackData.filter(F.action == 'statistics'))
# async def statistics(call: CallbackQuery, callback_data: MyAccountCallBackData):
#     text = f'Здесь будет выводиться история ваших заказов'
#     await call.answer(text)

# @account_info_router.message(MyAccountCallBackData.filter(F.action == 'price'))
# async def price(call: CallbackQuery, callback_data: MyAccountCallBackData):
#     text = f'Здесь будет выведена цена из базы'
#     await call.answer(text)
