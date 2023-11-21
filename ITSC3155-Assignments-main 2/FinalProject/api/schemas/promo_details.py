from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .guests import Guest


class PromoDetailBase(BaseModel):
    pass


class PromoDetailCreate(PromoDetailBase):
    promo_id: int
    guest_id: int


class PromoDetailUpdate(BaseModel):
    promo_id: Optional[int] = None
    guest_id: Optional[int] = None


class PromoDetail(PromoDetailBase):
    id: int
    promo_id: int
    guests: List[Guest] = None

    class ConfigDict:
        from_attributes = True