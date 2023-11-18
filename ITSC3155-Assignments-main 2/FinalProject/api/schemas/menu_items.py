from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .resources import Resource


class MenuItemBase(BaseModel):
    item: str
    price: float
    calories: int


class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    menu_id: Optional[int] = None

class MenuItem(MenuItemBase):
    id: int


    class ConfigDict:
        from_attributes = True
        