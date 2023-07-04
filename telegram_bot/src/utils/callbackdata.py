from aiogram.filters.callback_data import CallbackData


class AccountInfo(CallbackData, prefix='ikb'):
    action: str
