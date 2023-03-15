from aiogram.fsm.state import StatesGroup, State

class BuyBackStates(StatesGroup):
    key_word = State()
    product_card = State()
    buy_back_amount = State()
