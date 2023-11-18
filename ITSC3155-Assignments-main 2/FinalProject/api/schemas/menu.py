from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .resources import Resource


class MenuBase(BaseModel):
    item: str
    price: int
    calories: int


class MenuCreate(MenuBase):
    pass

class MenuUpdate(BaseModel):
    menu_id: Optional[int] = None

class Menu(MenuBase):
    id: int


    class ConfigDict:
        from_attributes = True
        