from .base import Base
from typing import Optional
import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


class User(Base):
    __tablename__ = 'user_account'

    # Айди юзера
    user_id: Mapped[int] = mapped_column(unique=True, nullable=False)

    # Никнейм в телеге
    user_name: Mapped[Optional[str]] = mapped_column(unique=False, nullable=True)

    # Дата регистрации
    reg_date: Mapped[int] = mapped_column(default=datetime.date.today())

    # Дата последнего обновления
    upd_date: Mapped[int] = mapped_column(onupdate=datetime.date.today())
    
    # Заказ
    buyback: Mapped[int] = mapped_column(ForeignKey("buyback_data.id"))

    # Баланс
    balance: Mapped[int] =  mapped_column(nullable=True)

    def __str__(self) -> str:
        return f'<User:{self.user_id}>'