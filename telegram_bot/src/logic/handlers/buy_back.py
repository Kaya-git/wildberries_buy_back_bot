from aiogram.types import Message
from aiogram.filters import Text
from ..fsm.finite_st_buyback import BuyBackStates
from aiogram import Router
from ..keyboards.reply import kb_main_menu, cancel_button
from ..fsm.finite_st_buyback import BuyBackStates
from aiogram.fsm.context import FSMContext
import logging
from database import Database
from src.middlewares import DatabaseMiddleware
from sqlalchemy import insert


buyback_router = Router(name="buyback")
buyback_router.message.middleware(DatabaseMiddleware())


@buyback_router.message(Text(text=['Самовыкуп'], ignore_case=True))
async def start_buy_back(message: Message, state: FSMContext) -> None:
    """
    Обрабатываем команду сбора и информации для самовыкупа, ожидаем ввод ключевого слова от пользователя
    """
    await state.set_state(BuyBackStates.key_word)
    await message.answer(
        text='Отправте в чат ключевое слово, по которому вы хотите продвинуться.'
        'Обязательно убедитесь в корректности орфографии',
        reply_markup=cancel_button
    )


@buyback_router.message(Text(text=['Отмена']))
async def cancel(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    
    logging.info("Cancelling state %r", current_state)
    await state.clear()

    await message.answer(
        text='Отмена',
        reply_markup=kb_main_menu
    )
    await message.delete()


@buyback_router.message(BuyBackStates.key_word)
async def load_product_link(message: Message, state: FSMContext):
    await state.update_data(key_word=message.text)
    await state.set_state(BuyBackStates.product_link)
    await message.reply(
        "Скинь ссылку на страницу продукта, для продвижения",
        reply_markup=cancel_button
    )


@buyback_router.message(BuyBackStates.product_link)
async def item_size(message: Message, state: FSMContext):
    await state.update_data(product_link=message.text)
    await state.set_state(BuyBackStates.item_size)
    await message.reply(
        'Укажи размер товара',
        reply_markup=cancel_button
    )


@buyback_router.message(BuyBackStates.item_size)
async def buy_back_amount(message: Message, state: FSMContext):
    await state.update_data(item_size=message.text)
    await state.set_state(BuyBackStates.bb_amount)
    await message.reply(
        'Укажи кол-во требуемых выкупов',
        reply_markup=cancel_button
    )


@buyback_router.message(BuyBackStates.bb_amount)
async def lets_ride(message: Message, state: FSMContext, db: Database):
    await state.update_data(bb_amount=message.text)
    user_data = await state.get_data()
    key_word = user_data["key_word"]
    product_link = user_data["product_link"]
    item_size = user_data["item_size"]
    bb_amount = user_data["bb_amount"]
    user_id = message.from_user.id
    
    # new_bb = await db.buyback.new(
    #     key_word=key_word,
    #     product_link=product_link,
    #     item_size=item_size,
    #     bb_amount=bb_amount,
    #     user_id=user_id)
    # print("ВЫКУП")
    # await db.session.commit()
    await message.reply(
        f"(Ваш заказ по ключевому слову {key_word}//"
        f"ссылка на товар {product_link}//"
        f"размер товара {item_size}//"
        f"кол-во выкупов {bb_amount})",
        reply_markup=kb_main_menu
    )
    
    await state.clear()
