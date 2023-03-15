from aiogram.types import Message
from keyboards.reply import kb_main_menu, cancel_button
from finite_state_machine.finite_st_buyback import BuyBackStates
from aiogram.fsm.context import FSMContext
import logging

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


async def load_product_card(message: Message, state: FSMContext):
    await state.update_data(key_word=message.text)
    await state.set_state(BuyBackStates.product_card)
    await message.reply(
        "Загрузи карточку для самовыкупа, как указанно в примере",
        reply_markup=cancel_button
    )


async def buyback_amount(message: Message, state: FSMContext):
    await state.update_data(product_card=message.photo[0].file_id)
    await state.set_state(BuyBackStates.buy_back_amount)
    await message.reply(
        'Укажи кол-во самовыкупов',
        reply_markup=cancel_button
    )


async def lets_ride(message: Message, state: FSMContext):
    await state.update_data(buy_back_amount=message.text)
    await state.clear()
    await message.reply(
        "Готово",
        reply_markup=kb_main_menu
    )
