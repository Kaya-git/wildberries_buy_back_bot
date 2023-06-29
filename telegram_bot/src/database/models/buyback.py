from .base import Base
from typing import Optional
import datetime
from sqlalchemy.orm import Mapped, mapped_column


class BuyBack(Base):
    __tablename__ = 'buyback_data'

    # Ключевое слово для продвижения
    key_word: Mapped[str] = mapped_column(unique=False, nullable=False)

    # Ссылка на товар
    product_link: Mapped[str] = mapped_column(unique=False, nullable=False)

    # Размер товара
    item_size: Mapped[Optional[str]] = mapped_column(nullable=True)

    # Кол-во самовыкупов
    bb_amount: Mapped[int] = mapped_column(unique=False, nullable=False)

    def __str__(self) -> str:
        return f'<buyback: {self.id}'
