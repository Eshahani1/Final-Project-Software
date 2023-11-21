from typing import Optional
from pydantic import BaseModel

class GuestBase(BaseModel):
    name: str
    payment_id: int
    order_id: int
    promo_id: int
    phone_number: str
    address: str

class GuestCreate(GuestBase):
    pass

class GuestUpdate(BaseModel):
    name: Optional[str] = None
    payment_id: Optional[int] = None
    order_id: Optional[int] = None
    promo_id: Optional[int] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None

class Guest(GuestBase):
    id: int

class ConfigDict:
    from_attributes = True
