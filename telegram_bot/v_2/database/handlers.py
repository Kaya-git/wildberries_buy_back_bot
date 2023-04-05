from sqlalchemy.orm import sessionmaker


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
        buyback = Bu

