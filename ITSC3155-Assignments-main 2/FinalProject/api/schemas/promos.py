from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .promos import Promo


class PromoBase(BaseModel):
    code: str
    menu_id: int
    discount: int


class PromoCreate(PromoBase):
    pass


class PromoUpdate(PromoBase):
    code: Optional[str] = None
    menu_id: Optional[int] = None
    discount: Optional[int] = None


class Promo(PromoBase):
    code: str
    menu_id: int
    discount: int

    class ConfigDict:
        from_attributes = True
