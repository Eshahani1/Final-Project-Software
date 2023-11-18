from typing import Optional
from pydantic import BaseModel
from .orders import Order

class GuestBase(BaseModel):
    name: str
    phone_number: str
    address: str

class GuestCreate(GuestBase):
    pass

class GuestUpdate(BaseModel):
    name: Optional[str] = None
    order_id: Optional[int] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None

class Guest(GuestBase):
    id: int
    orders: list[Order] = None

    class ConfigDict:
        from_attributes = True
