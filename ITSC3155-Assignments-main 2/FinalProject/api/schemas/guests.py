from typing import Optional
from pydantic import BaseModel
from .orders import Order
from .payments import Payment


class GuestBase(BaseModel):
    name: str
    phone_number: int
    address: str
    email: str


class GuestCreate(GuestBase):
    pass


class GuestUpdate(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[int] = None
    address: Optional[str] = None
    email: Optional[str] = None


class Guest(GuestBase):
    id: int
    orders: list[Order] = None
    payments: list[Payment] = None

    class ConfigDict:
        from_attributes = True
