from .base import BaseModel
from typing import List, Optional
import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


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

    class BuyBack(BaseModel):
        __tablename__ = 'buyback_data'

        # Buyback id
        id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

        # Telegram user id
        user_id: Mapped[int] = mapped_column(ForeignKey("user_account.user_id"))

        # Keyword for buyback
        wb_keyword: Mapped[str] = mapped_column(unique=False, nullable=False)

        # Product card URL
        pc_url: Mapped[str] = mapped_column(unique=False, nullable=False)

        # Buyback amount
        ordered_amount: Mapped[int] = mapped_column(unique=False, nullable=False)

        # Amount of approved buybacks
        approved_amount: Mapped[int] = mapped_column(unique=False, nullable=True)

        def __str__(self) -> str:
            return f'<buyback: {self.id}'
