from .base import BaseModel
from typing import List, Optional
import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from telegram_bot.v_2.database.buyback import BuyBack


class User(BaseModel):
    __tablename__ = 'user_account'

    # Telegram user id
    user_id: Mapped[int] = mapped_column(primary_key=True, unique=True)

    # Telegram user name
    user_name: Mapped[Optional[str]] = mapped_column(unique=False)

    # User balance
    balance: Mapped[Optional[int]] = mapped_column(unique=False)

    # Buyback data
    buyback: Mapped[List["BuyBack"]] = relationship()

    # Registration date
    reg_date: Mapped[int] = mapped_column(default=datetime.date.today())

    # Last update date
    upd_date: Mapped[int] = mapped_column(onupdate=datetime.date.today())

    def __str__(self) -> str:
        return f'<User:{self.user_id}>'
