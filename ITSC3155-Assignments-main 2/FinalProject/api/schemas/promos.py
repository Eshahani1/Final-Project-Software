from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .promo_details import PromoDetail


class PromoBase(BaseModel):
    code: str
    discount: float
    expiration_date: datetime


class PromoCreate(PromoBase):
    pass


class PromoUpdate(PromoBase):
    code: Optional[str] = None
    discount: Optional[float] = None
    expiration_date: Optional[datetime] = None


class Promo(PromoBase):
    id: int
    code: str
    discount: float
    promo_details: list[PromoDetail] = None

    class ConfigDict:
        from_attributes = True
