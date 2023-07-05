from .base import Base
from typing import Optional
import datetime
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = 'user'

    # Айди юзера в телеграмме
    user_id: Mapped[int] = mapped_column(primary_key=True, unique=True, nullable=False)

    # Никнейм в телеге
    user_name: Mapped[Optional[str]] = mapped_column(unique=False, nullable=True)

    # Баланс
    balance: Mapped[int] =  mapped_column(default=0, nullable=True)

    def __str__(self) -> str:
        return f'<User:{self.user_id}>'