from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .order_details import OrderDetail


class OrderBase(BaseModel):
    tracking_nums: int
    order_status: str
    card_number: int
    pin: int
    method: str
    transaction_status: str
    order_preference: str
    promo_code: Optional[str] = None
    total_cost: Optional[float] = None


class OrderCreate(OrderBase):
    guest_id: int
    promo_code: str


class OrderUpdate(BaseModel):
    guest_id: Optional[int] = None
    promo_code: Optional[str] = None
    tracking_nums: Optional[int] = None
    order_status: Optional[str] = None
    card_number: Optional[int] = None
    pin: Optional[int] = None
    method: Optional[str] = None
    transaction_status: Optional[str] = None
    order_preference: Optional[str] = None
    total_cost: Optional[float] = None

class Order(OrderBase):
    id: int
    guest_id: int
    promo_code: str
    order_date: Optional[datetime] = None
    order_details: Optional[List[OrderDetail]] = None
    order_preference: Optional[str] = None

    class Config:
        from_attributes = True
