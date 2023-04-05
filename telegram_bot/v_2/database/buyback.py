from .base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from telegram_bot.v_2.database.user import User

class BuyBack(BaseModel):
    __tablename__ = 'buyback_data'

    # Buyback id
    id: Mapped[int] = mapped_column(primary_key=True)

    # Telegram user id
    user_id: Mapped[int] = mapped_column(Foreignkey(user_account.id))


    # Keyword for buyback
    wb_keyword

    # Product card URL
    pc_url

    # Buyback amount
    ordered_amount

    # Amount of approved buybacks
    approved_amount