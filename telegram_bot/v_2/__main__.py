from aiogram import Dispatcher, Bot
from  config import BOT_TOKEN
from commands import register_user_commands
from commands.bot_commands import bot_commands
import logging
import asyncio
from aiogram.types import BotCommand
from sqlalchemy.engine import URL
from database import BaseModel, create_async_engine, get_session_maker, proceed_schemas

async def main():
    logging.basicConfig(level=logging.DEBUG)

    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))

    dp = Dispatcher()
    bot = Bot(
        token=BOT_TOKEN,
        parse_mode='HTML'
    )
    await bot.set_my_commands(commands=commands_for_bot)

    register_user_commands(dp)

    postgres_url = URL.create(
        "postgresql+asyncpg",
        username="postgres",
        host="localhost",
        password="WW9JUQhP",
        database="BuyBackBase",
        port="5432"
    )

    async_engine = create_async_engine(postgres_url)
    session_maker = get_session_maker(async_engine)
    await proceed_schemas(async_engine, BaseModel.metadata)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
