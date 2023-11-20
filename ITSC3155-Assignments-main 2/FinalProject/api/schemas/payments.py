from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PaymentBase(BaseModel):
    number: int
    pin: int
    type: str


class PaymentCreate(PaymentBase):
    guest_id: int


class PaymentUpdate(BaseModel):
    number: Optional[int] = None
    pin: Optional[int] = None
    type: Optional[str] = None
    guest_id: Optional[int] = None


class Payment(PaymentBase):
    id: int
    guest_id: int

    class ConfigDict:
        from_attributes = True