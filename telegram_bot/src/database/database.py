from typing import Union

from sqlalchemy import MetaData
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker

from .CRUD.user import UserRepo
from .CRUD.buyback import BuybackRepo


def create_async_engine(url: Union[URL, str]) -> AsyncEngine:
    return _create_async_engine(url=url, echo=True, pool_pre_ping=True)


async def proceed_schemas(engine: AsyncEngine, metadata: MetaData) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


def get_session_maker(engine: AsyncEngine) -> sessionmaker:
    return sessionmaker(engine, class_=AsyncEngine)


class Database:
    """
    Database class is the highest abstraction level of database
    and can be used in the handlers or any other bot-side functions
    """
    
    user: UserRepo
    """ User repository"""
    
    buyback: BuybackRepo
    """ Buy back order repository"""
    
    session: AsyncSession
    
    def __init__(
        self,
        session: AsyncSession,
        user: UserRepo = None,
        buyback: BuybackRepo = None
        ) -> None:
        self.session = session
        self.user = user or UserRepo(session=session)
        self.buyback = buyback or BuybackRepo(session=session)