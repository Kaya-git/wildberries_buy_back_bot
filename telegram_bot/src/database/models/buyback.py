from .base import Base
from typing import Optional
import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


class BuyBack(Base):
    __tablename__ = 'buyback'

    # Ключевое слово для продвижения
    key_word: Mapped[str] = mapped_column(unique=False, nullable=False)

    # Ссылка на товар
    product_link: Mapped[str] = mapped_column(unique=False, nullable=False)

    # Размер товара
    item_size: Mapped[Optional[str]] = mapped_column(nullable=True)

    # Кол-во самовыкупов
    bb_amount: Mapped[int] = mapped_column(unique=False, nullable=False)
    
    # Айди пользователя
    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id", ondelete="CASCADE"))

    def __str__(self) -> str:
        return f'<buyback: {self.id}'
