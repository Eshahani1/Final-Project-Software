from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PaymentBase(BaseModel):
    card_number: int
    pin: int
    method: str


class PaymentCreate(PaymentBase):
    guest_id: int


class PaymentUpdate(BaseModel):
    card_number: Optional[str] = None
    pin: Optional[int] = None
    method: Optional[str] = None
    guest_id: Optional[int] = None


class Payment(PaymentBase):
    id: int
    guest_id: int

    class ConfigDict:
        from_attributes = True