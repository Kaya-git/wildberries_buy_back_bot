# from .base import BaseModel
# from typing import List, Optional
# from sqlalchemy import ForeignKey, String
# from database.user import User
# import datetime
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# class BuyStat(BaseModel):
#     __tablename__ = 'buyback'

#     #Id
#     id: Mapped[int] = mapped_column(primary_key=True)

#     #User id
#     user_id: Mapped[int] = mapped_column(ForeignKey("user_account.user_id"))

#     #Key word in search tab
#     key_word: Mapped[str] = mapped_column(unique=False, nullable=False)

#     #Id of product card photo
#     prod_card: Mapped[str] = mapped_column(unique=True, nullable=False)

#     #Amount of buybacks
#     amount: Mapped[int] = mapped_column(unique=False, nullable=False)

#     #Product price
#     price: Mapped[int] = mapped_column()
