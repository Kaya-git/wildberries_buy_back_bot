__all__ = ['register_user_commands',]

from aiogram import Router
from commands.start import start, my_account
from commands.help import help
from commands.buy_back import start_buy_back, cancel
# from commands.my_account import go_to_balance, go_to_stat, go_to_prices
from commands.referals import share
from aiogram.filters.command import Command
from aiogram.filters import Text


def register_user_commands(router: Router) -> None:
    router.message.register(start, Command(commands=['start']))
    router.message.register(help, Command(commands=['help']))

    router.message.register(start_buy_back, Text(text=['Самовыкуп'], ignore_case=True))
    router.message.register(my_account, Text(text=['Настройки']))
    router.message.register(share, Text(text=['Рефералка']))

    router.message.register(cancel, Text(text=['Отмена']))

    # router.callback_query.register(go_to_balance, BuyBackCallBackData.filter(action='balance'))
    # router.callback_query.register(go_to_stat, BuyBackCallBackData.filter(action='statistics'))
    # router.callback_query.register(go_to_prices, BuyBackCallBackData.filter(action='balance'))
