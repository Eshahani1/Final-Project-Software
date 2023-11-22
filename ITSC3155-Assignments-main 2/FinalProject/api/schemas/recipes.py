from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .resources import Resource


class RecipeBase(BaseModel):
    amount: int


class RecipeCreate(RecipeBase):
<<<<<<< HEAD
    resource_id: int
    menu_id: int
||||||| 69af943
    sandwich_id: int
    menu_id: int
=======
    menu_item_id: int
    resource_id: int
>>>>>>> database-alteration

class RecipeUpdate(BaseModel):
    menu_item_id: Optional[int] = None
    resource_id: Optional[int] = None
    amount: Optional[int] = None

class Recipe(RecipeBase):
    id: int
    menu_item_id: int
    resource: Resource = None

    class ConfigDict:
        from_attributes = True
