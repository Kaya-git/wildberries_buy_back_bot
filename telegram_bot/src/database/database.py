from typing import Union


from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.config import conf
from .repositories.user import UserRepo
from .repositories.buyback import BuybackRepo


def create_async_engine(url: Union[URL, str]) -> AsyncEngine:
    """
    :param url:
    :return:
    """
    return _create_async_engine(
        url=url, echo=conf.debug,
        pool_pre_ping=True
    )


def create_session_maker(engine: AsyncEngine = None) -> sessionmaker:
    """
    :param url:
    :return:
    """
    return sessionmaker(
        engine or create_async_engine(conf.db.build_connection_str()),
        class_=AsyncSession,
        expire_on_commit=False
    )

class Database:
    """
    Database class is the highest abstraction level of database
    and can be used in the handlers or any other bot-side functions
    """
    
    user: UserRepo
    """ User repository """
    
    buyback: BuybackRepo
    """ Buy back order repository """
    
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
        