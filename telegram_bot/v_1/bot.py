import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN

from database import BaseModel, create_async_engine, get_session_maker, proceed_schemas

from sqlalchemy.engine import URL

# from postgresql import db_start


# async def on_startup(_):
#     await db_start()


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


postgres_url = URL.create(
    "postgresql+asyncpg",
    username='postgres',
    host="localhost",
    password='WW9JUQhP',
    database='buy_back_bot',
    port=5432
)

async_engine = create_async_engine(postgres_url)
sesion_maker = get_session_maker(async_engine)
proceed_schemas(async_engine, BaseModel.metadata)


if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(
        dp,
        skip_updates=True,
    )
