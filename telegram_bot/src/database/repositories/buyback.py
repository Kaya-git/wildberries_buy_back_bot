"""Buyback repository file"""
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import BuyBack
from .abstract import Repository


class BuybackRepo(Repository[BuyBack]):
    """
    Buyback repository for CRUD and other SQL queries
    """
    def __init__(self, session: AsyncSession):
        """
        Initialize user repository as for all buybacks or only for one buyback
        """
        super().__init__(type_model=BuyBack, session=session)
    
    async def new(
        self,
        buyback_id: int,
        key_word: str = None,
        product_link: str = None,
        item_size: Optional[str] = None,
        bb_amount: int = None,
    ) -> None:
        """
        Insert a new user into the database
        :param buyback_id: Telegram buyback id
        :param key_word: Buyback keyword
        :param product_link: Product link
        :param item_size: Item size if necessary
        :param bb_amount: Amount of needed buybacks
        """
        new_buyback = await self.session.merge(
            BuyBack(
                buyback_id=buyback_id,
                key_word=key_word,
                product_link=product_link,
                item_size=item_size,
                bb_amount=bb_amount,
            )
        )
        return new_buyback