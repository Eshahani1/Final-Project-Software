from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail


class OrderBase(BaseModel):
    tracking_nums: int
    status: str


class OrderCreate(OrderBase):
   guest_id: int


class OrderUpdate(BaseModel):
    guest_id: Optional[int] = None
    tracking_num: Optional[int] = None
    status: Optional[str] = None


class Order(OrderBase):
    id: int
    guest_id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
