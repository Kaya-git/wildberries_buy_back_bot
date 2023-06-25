from .commands.start import start_router
from .commands.help import help_router
from .handlers.buy_back import buyback_router
from .handlers.my_account import account_info_router
from .handlers.referals import referals_router


routers = (start_router, buyback_router, help_router, account_info_router, referals_router)
