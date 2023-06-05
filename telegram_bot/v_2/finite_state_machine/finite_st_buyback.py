from aiogram.fsm.state import StatesGroup, State


class BuyBackStates(StatesGroup):
    key_word = State()
    product_link = State()
    buy_back_amount = State()
    item_size = State()
    bb_amount = State()
