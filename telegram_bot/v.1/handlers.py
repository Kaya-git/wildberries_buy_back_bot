from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command

from keyboards import keyboard_main, keyboard_my_ac

from bot import bot, dp


@dp.message_handler(commands=['start'])
async def main_menu(message: Message):
    await message.answer('Главное меню', reply_markup=keyboard_main)


@dp.message_handler(Text(equals=['Самовыкуп']))
async def start_buy_back(message: Message):
    await message.answer(message.text)


@dp.message_handler(Text(equals=['Настройки']))
async def go_to_my_ac(message: Message):
    await message.answer( text='Настройки', reply_markup=keyboard_my_ac)


@dp.message_handler(commands=['settings'])
async def go_to_my_ac_comand(message: Message):
    await message.answer( text='Настройки', reply_markup=keyboard_my_ac)

