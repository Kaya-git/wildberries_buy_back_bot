from aiogram.filters.callback_data import CallbackData

# cb = CallbackData('ikb', 'action')
class BuyBackCallBackData(CallbackData, prefix='ikb'):
    action: str
