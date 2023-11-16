from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class OrderBase(BaseModel):
    guest_name: str
    order_date: str
    order_details_id: int
    tracking_nums: int
    status: str


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    guest_name: Optional[str] = None
    order_date: Optional[str] = None
    order_details_id: Optional[str] = None
    tracking_nums: Optional[str] = None
    status: Optional[str] = None

class Order(OrderBase):
    id: int

    class ConfigDict:
        from_attributes = True
