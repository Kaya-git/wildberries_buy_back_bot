from aiogram.fsm.state import StatesGroup, State


class BuyBackStates(StatesGroup):
    key_word = State()
    product_link = State()
    item_size = State()
    bb_amount = State()
