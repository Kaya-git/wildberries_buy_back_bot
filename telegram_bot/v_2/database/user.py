from .base import BaseModel
from typing import List, Optional
from sqlalchemy import ForeignKey, String
import datetime
# from database.stat_data import BuyStat
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class User(BaseModel):
    __tablename__ = 'user_account'

    # Telegram user id
    user_id: Mapped[int] = mapped_column( primary_key=True, unique=True)

    # Telegram user name
    user_name: Mapped[Optional[str]] = mapped_column(unique=False)

    # User balance
    balance: Mapped[Optional[int]] = mapped_column(unique=False)

    # User history
    # buy_stat: Mapped[List["BuyStat"]] = relationship(back_populates="User", cascade="all, delete-orphan")

    # Registration date
    reg_date: Mapped[int] = mapped_column(default=datetime.date.today())

    # Last update date
    upd_date: Mapped[int] = mapped_column(onupdate=datetime.date.today())

    def __str__(self) -> str:
        return f'<User:{self.user_id}>'
