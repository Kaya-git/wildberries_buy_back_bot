# __all__ = ['register_user_commands',]

# from aiogram import Router, F
# from commands.start import start
# from commands.help import help
# from handlers.buy_back import start_buy_back, cancel, load_product_link, item_size, buy_back_amount, lets_ride
# from handlers.my_account import my_account
# from handlers.callback import balance, statistics, price
# from handlers.referals import share
# from aiogram.filters.command import Command
# from aiogram.filters import Text
# from utils.callbackdata import MyAccountCallBackData
# from fsm.finite_st_buyback import BuyBackStates


# def register_user_commands(router: Router) -> None:
    # router.message.register(start, Command(commands=['start']))
    # router.message.register(help, Command(commands=['help']))

    # router.message.register(start_buy_back, Text(text=['Самовыкуп'], ignore_case=True))
    # router.message.register(my_account, Text(text=['Настройки']))
    # router.message.register(share, Text(text=['Рефералка']))

    # router.message.register(cancel, Text(text=['Отмена']))

    # router.callback_query.register(balance, MyAccountCallBackData.filter(F.action == 'balance'))
    # router.callback_query.register(statistics, MyAccountCallBackData.filter(F.action == 'statistics'))
    # router.callback_query.register(price, MyAccountCallBackData.filter(F.action == 'price'))

    # router.message.register(load_product_link, BuyBackStates.key_word)
    # router.message.register(item_size, BuyBackStates.product_link)
    # router.message.register(buy_back_amount, BuyBackStates.item_size)
    # router.message.register(lets_ride, BuyBackStates.bb_amount)
