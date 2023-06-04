from .base import BaseModel
from typing import List, Optional
import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


class BuyBack(BaseModel):
    __tablename__ = 'buyback_data'

    # Айди заказа
    id: Mapped[int] = mapped_column(primary_key=True)

    # Ключевое слово для продвижения
    wb_keyword: Mapped[str] = mapped_column(unique=False, nullable=False)

    # Ссылка на товар
    item_number: Mapped[str] = mapped_column(unique=False, nullable=False)

    # Цвет товара
    item_colour: Mapped[Optional[str]] = mapped_column()

    # Размер товара
    item_size: Mapped[Optional[str]] = mapped_column()

    # Кол-во самовыкупов
    ordered_amount: Mapped[int] = mapped_column(unique=False, nullable=False)

    def __str__(self) -> str:
        return f'<buyback: {self.id}'


class User(BaseModel):
    __tablename__ = 'user_account'

    # Айди юзера
    user_id: Mapped[int] = mapped_column(primary_key=True, unique=True)

    # Никнейм в телеге
    user_name: Mapped[Optional[str]] = mapped_column(unique=False)

    # Дата регистрации
    reg_date: Mapped[int] = mapped_column(default=datetime.date.today())

    # Дата последнего обновления
    upd_date: Mapped[int] = mapped_column(onupdate=datetime.date.today())
    
    # Заказ
    order: Mapped[int] = mapped_column(ForeignKey("buyback_data.id"))

    # Баланс
    balance: Mapped[int] =  mapped_column(nullable=True)

    def __str__(self) -> str:
        return f'<User:{self.user_id}>'



