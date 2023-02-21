import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN

storage = MemoryStorage()
loop = asyncio.new_event_loop()
bot = Bot(
    BOT_TOKEN,
    parse_mode='HTML',
)
dp = Dispatcher(
    bot,
    storage=storage,
    loop=loop,
)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(
        dp,
        skip_updates=True,)
