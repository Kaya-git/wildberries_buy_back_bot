""" User repository file """
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from ..models import User
from .abstract import Repository


class UserRepo(Repository[User]):
    """
    User repository for CRUD and other SQL queries
    """

    def __init__(self, session: AsyncSession):
        """
        Initialize user repository as for all users or only for one user
        """
        super().__init__(type_model=User, session=session)

    async def new(
        self,
        user_id: int,
        user_name: Optional[str] = None,
        balance: Optional[int] = None
        # reg_date: Optional[int] = None,
        # upd_date: Optional[int] = None,
    ) -> None:
        """
        Insert a new user into the database
        :param user_id: Telegram user id
        :param user_name: Telegram username
        :param reg_date: Register date
        :param upd_date: Account last update date
        :param buyback: User buyback orders
        :param user_balance: User balance
        """
        new_user = await self.session.merge(
            User(
                user_id=user_id,
                user_name=user_name,
                balance=balance,
                # reg_date=reg_date,
                # upd_date=upd_date,
            )
        )
        return new_user
    