from database.db import BaseModel
from sqlalchemy import Column, Integer, VARCHAR, Date
from datetime import date

class User(BaseModel):
    __tablename__ = 'users'

    #telegram user id
    user_id = Column(Integer, unique=True, nullable=False, primary_key=True)

    #telegram user name
    user_name = Column(VARCHAR, unique=False, nullable=True)

    #Registration date
    reg_date = Column(Date, default=date.today())

    #Last update date
    upd_date = Column(Date, onupdate=date.today())


    def __str__(self) -> str:
        return f'User:{self.user_id}'
