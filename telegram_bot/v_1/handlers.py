from aiogram.types import Message, CallbackQuery
from aiogram.filters.state import StatesGroup, State
from aiogram.filters import Text, Command
from aiogram.dispatcher import FSMContext

from keyboards import kb_main, kb_acount, cancel_button, cb

from bot import bot, dp


# from postgresql import db_start, create_rofile, edit_profile

class ClientStateGroup(StatesGroup):
    key_word = State()
    product_card = State()
    buy_back_amount = State()
    question = State()


@dp.message_handler(commands=['start'])
async def main_menu(message: Message) -> None:
    """
    Хендлер на команду старта
    """

    await message.answer('Главное меню', reply_markup=kb_main)
    await message.delete()

    # await create_rofile(user_id=message.from_user.id)


@dp.message_handler(Text(equals=['Самовыкуп'], ignore_case=True), state=None)
async def start_buy_back(message: Message) -> None:
    """
    Обрабатываем команду сбора и информации для самовыкупа, ожидаем ввод ключевого слова от пользователя
    """

    await ClientStateGroup.key_word.set()
    await message.answer(
        text='Отправте в чат ключевое слово, по которому вы хотите продвинуться.'
        'Обязательно убедитесь в корректности орфографии',
        reply_markup=cancel_button
    )


@dp.message_handler(Text(equals='Отмена'), state='*')
async def cancel(message: Message, state: FSMContext):

    current_state = state.get_state()
    if current_state is None:
        return
    
    await message.answer(
        text='Отмена',
        reply_markup=kb_main
    )
    await message.delete()
    await state.finish()


@dp.message_handler( state=ClientStateGroup.key_word)
async def load_product_card(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['key_word'] = message.text
    
    await ClientStateGroup.next()
    await message.reply(
        text='А теперь давай загрузим карточку для самовыкупа',
        reply_markup=cancel_button
    )


@dp.message_handler(lambda message: message.photo, content_types=['photo'], state=ClientStateGroup.product_card)
async def load_product_card(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_card'] = message.photo[0].file_id
    
    await ClientStateGroup.next()
    await message.reply(
        text='А теперь давай укажем сумму для самовыкупа',
        reply_markup=cancel_button
    )


@dp.message_handler(lambda message: not message.photo, state=ClientStateGroup.product_card)
async def check_product_card(message: Message):
    await message.reply('Это не карточка товара')


@dp.message_handler(state=ClientStateGroup.buy_back_amount)
async def load_product_card(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['buy_back_amount'] = message.text


    async with state.proxy() as data:
        print(data)
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=data['product_card'],
            caption= f"Товар будет выкуплен в категории {data['key_word']}, на сумму {data['buy_back_amount']}",
            reply_markup=kb_main
        )
    # await edit_profile(state, user_id=message.from_user.id)
    await state.finish()


@dp.message_handler(Text(equals=['Настройки']))
async def my_account(message: Message) -> None:
    """
    Обрабатываем настройки
    """

    await message.answer(
        text='Настройки',
        reply_markup=kb_acount
    )
    await message.delete()


@dp.message_handler(Text(equals=['Поделиться']))
async def share(message: Message) -> None:
    """
    Обрабатываем команду пригласить друга
    """

    await message.answer(
        text='В дальнейшем стоит добавить реферальную ссылку и добавлять на баланс деньги,'
        'если пользователь которого добавили, пополнит баланс',
        reply_markup=kb_main
    )


@dp.message_handler(commands=['settings'])
async def go_to_my_ac_comand(message: Message) -> None:
    """
    Обрабатываем команду на вход в лк
    """

    await message.answer(
        text='Настройки',
        reply_markup=kb_acount
    )
    await message.delete()


@dp.callback_query_handler(cb.filter(action='balance'))
async def go_to_balance(callback: CallbackQuery) -> None:
    """
    Обрабатываем команду просмотра баланса
    """

    await callback.answer(
        show_alert=True,
        text='Твой баланс на текущий момент равено 0.'
    )


@dp.callback_query_handler(cb.filter(action='statistics'))
async def go_to_stat(callback: CallbackQuery) -> None:
    """
    Обрабатываем команду статистики
    """

    await callback.answer(
        show_alert=True,
        text='Тут мы выведем таблицу с историей твоих выкупов.'
    )


@dp.callback_query_handler(cb.filter(action='ask_question'))
async def ask_question(callback: CallbackQuery) -> None:
    """
    Обрабатываем команду задат вопрос
    """

    await callback.answer(
        show_alert=True,
        text='Напиши свой вопрос, тебе ответят в ближайщее время.'
    )
    await bot.send_message(
        chat_id='327758170',
        text='Пришел вопрос'
    )


@dp.callback_query_handler(cb.filter(action='prices'))
async def go_to_prices(callback: CallbackQuery) -> None:
    """
    Вывести цены
    """

    await callback.answer(
        show_alert=True,
        text='Цена одного выкупа составляет 70 руб'
    )
