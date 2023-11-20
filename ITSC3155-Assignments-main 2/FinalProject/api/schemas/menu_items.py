from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .resources import Resource


class MenuItemBase(BaseModel):
    item: str
    price: int
    calories: int


class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    menu_id: Optional[int] = None

class Menu(MenuItemBase):
    id: int


    class ConfigDict:
        from_attributes = True
        