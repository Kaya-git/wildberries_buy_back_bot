__all__ = ['register_user_commands',]

from aiogram import Router, F
from telegram_bot.v_2.commands.start import start
from telegram_bot.v_2.commands.help import help
from telegram_bot.v_2.handlers.buy_back import start_buy_back, cancel, load_product_card, buyback_amount, lets_ride
from telegram_bot.v_2.handlers.my_account import my_account
from telegram_bot.v_2.handlers.callback import balance, statistics, price
from telegram_bot.v_2.handlers.referals import share
from aiogram.filters.command import Command
from aiogram.filters import Text
from telegram_bot.v_2.utils.callbackdata import MyAccountCallBackData
from telegram_bot.v_2.finite_state_machine.finite_st_buyback import BuyBackStates


def register_user_commands(router: Router) -> None:
    router.message.register(start, Command(commands=['start']))
    router.message.register(help, Command(commands=['help']))

    router.message.register(start_buy_back, Text(text=['Самовыкуп'], ignore_case=True))
    router.message.register(my_account, Text(text=['Настройки']))
    router.message.register(share, Text(text=['Рефералка']))

    router.message.register(cancel, Text(text=['Отмена']))

    router.callback_query.register(balance, MyAccountCallBackData.filter(F.action == 'balance'))
    router.callback_query.register(statistics, MyAccountCallBackData.filter(F.action == 'statistics'))
    router.callback_query.register(price, MyAccountCallBackData.filter(F.action == 'price'))

    router.message.register(load_product_card, BuyBackStates.key_word)
    router.message.register(buyback_amount, BuyBackStates.product_card)
    router.message.register(lets_ride, BuyBackStates.buy_back_amount)
