from aiogram import Dispatcher, Bot
from rq import Queue
from config import (
    BOT_TOKEN,
    bd_host,
    bd_username,
    bd_pass,
    bd_database,
    bd_port
)
from commands import register_user_commands
from commands.bot_commands import bot_commands
import logging
import asyncio
from aiogram.types import BotCommand
from sqlalchemy.engine import URL
from database import (
    BaseModel,
    create_async_engine,
    get_session_maker,
    proceed_schemas
)
import redis.asyncio as redis
from aiogram.fsm.storage.redis import RedisStorage


async def main():
    logging.basicConfig(level=logging.DEBUG)

    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))

    r = redis.Redis()
    q = Queue('work_queue', connection=r)

    dp = Dispatcher(storage=RedisStorage(redis=r))
    bot = Bot(
        token=BOT_TOKEN,
        parse_mode='HTML'
    )
    await bot.set_my_commands(commands=commands_for_bot)

    register_user_commands(dp)

    postgres_url = URL.create(
        "postgresql+asyncpg",
        username=bd_username,
        host=bd_host,
        password=bd_pass,
        database=bd_database,
        port=bd_port
    )

    async_engine = create_async_engine(postgres_url)
    session_maker = get_session_maker(async_engine)
    await proceed_schemas(async_engine, BaseModel.metadata)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
