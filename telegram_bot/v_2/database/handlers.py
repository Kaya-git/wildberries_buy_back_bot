from sqlalchemy.orm import sessionmaker
from .models import BuyBack

def create_buyback(
        session_maker: sessionmaker,
        user_id: int,
        wb_keyword: str,
        pc_url: str,
        ordered_amount: int,
        approved_amount: int
):
    """
    Create buyback record
    """
    async with session_maker() as session:
        async with session.begin():
        buyback = BuyBack(
            user_id=user_id,
            wb_keyword=wb_keyword,
            pc_url=pc_url,
            ordered_amount=ordered_amount,
            approved_amount=approved_amount
        )

