from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PromoBase(BaseModel):
    code: str
    menu_id: int
    discount: float


class PromoCreate(PromoBase):
    pass


class PromoUpdate(PromoBase):
    code: Optional[str] = None
    menu_id: Optional[int] = None
    discount: Optional[float] = None


class Promo(PromoBase):
    id: int
    code: str
    menu_id: int
    discount: float

    class ConfigDict:
        from_attributes = True
