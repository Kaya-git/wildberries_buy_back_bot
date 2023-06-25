from aiogram.filters.callback_data import CallbackData


class MyAccountCallBackData(CallbackData, prefix='ikb'):
    action: str
    text: str
