# from sqlalchemy.orm import sessionmaker
# from .models import BuyBack

# async def create_buyback(
#         session_maker: sessionmaker,
#         user_id: int,
#         wb_keyword,
#         item_link,
#         item_colour,
#         item_size,
#         ordered_amount
# ):
#     """
#     Create buyback record
#     """
#     async with session_maker() as session:
#         async with session.begin():
#         buyback = BuyBack(
#             user_id=user_id,
#             wb_keyword=wb_keyword,
#             item_link=item_link,
#             ordered_amount=ordered_amount,
#             item_colour=item_colour,
#             item_size=item_size
#         )
