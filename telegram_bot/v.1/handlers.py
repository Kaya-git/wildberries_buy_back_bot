from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command

from keyboards import keyboard_main, keyboard_my_ac, keyboard_buy_back

from bot import bot, dp

INFO = {
    'key_word': '',
    'amount': '',
    'pic_link': ''
}

@dp.message_handler(commands=['start'])
async def main_menu(message: Message):
    await message.answer('Главное меню', reply_markup=keyboard_main)
    await message.delete()


@dp.message_handler(Text(equals=['Самовыкуп']))
async def start_buy_back(message: Message):
    await message.answer('Отправте в чат ключевое слово, по которому вы хотите продвинуться.'
                         'Обязательно убедитесь в корректности орфографии'
                         'Указывать ключевое слово в формате "кс: ваше ключевое слово"',
                        )
    # await INFO['key_word'] = message.text
@dp.message_handler(Text(contains='кс:'))
async def key_word(message: Message):
    await message.answer('Ключевое слово добавлено.'
                         'Теперь напишите на какую сумму вы хотеть совершить самовыкупов.'
                         'Сумму пишите в формате "Сумма: ваша сумма"')
    INFO['key_word'] = message.text[4:]


@dp.message_handler(Text(equals='Сумма:'))
async def buy_back_sum(message: Message):
    await message.answer('Сумма добавлена.'
                         'Надеюсь у вас есть средства на балансе, либо сможете пополнить их с помощью кнопки.')

@dp.message_handler(Text(equals=['Настройки']))
async def my_account(message: Message):
    await message.answer( text='Настройки', reply_markup=keyboard_my_ac)
    await message.delete()


@dp.message_handler(Text(equals='Поделиться'))
async def share(message: Message):
    await message.answer(text='В дальнейшем стоит добавить реферальную ссылку и добавлять на баланс деньги,'
                           'если пользователь которого добавили, пополнит баланс',
                           reply_markup=keyboard_main
                           )


@dp.message_handler(Text(equals='Назад'))
async def go_back(message: Message):
    await message.answer( text='Назад', reply_markup=keyboard_main)
    await message.delete()

@dp.message_handler(commands=['settings'])
async def go_to_my_ac_comand(message: Message):
    await message.answer( text='Настройки', reply_markup=keyboard_my_ac)
    await message.delete()


@dp.callback_query_handler()
async def go_to_balance(callback: CallbackQuery):
    if callback.data == 'balance':
        await callback.answer('Твой баланс на текущий момент равено 0.')
    if callback.data =='statistics':
        await callback.answer('Тут мы выведем таблицу с историей твоих выкупов.')
    if callback.data == 'ask_question':
        await callback.answer('Напиши свой вопрос, тебе ответят в ближайщее время.')
        await bot.send_message(chat_id='327758170', text='Пришел вопрос')
    if callback.data == 'prices':
        await callback.answer(' Цена одного выкупа составляет 70 руб')