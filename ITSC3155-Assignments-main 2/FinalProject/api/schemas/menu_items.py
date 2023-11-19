from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .resources import Resource


class MenuItemBase(BaseModel):
    item_name: str
    category: str
    price: float
    calories: int


class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    item_name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None

class MenuItem(MenuItemBase):
    id: int


    class ConfigDict:
        from_attributes = True
        