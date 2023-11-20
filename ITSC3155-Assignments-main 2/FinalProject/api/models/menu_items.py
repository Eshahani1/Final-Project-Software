from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item_name = Column(String(100))
    price = Column(Integer, index=True, nullable=False)
    calories = Column(Integer, index=True, nullable=False)
    
    recipes = relationship("Recipe", back_populates="menu_items")
    order_details = relationship("OrderDetail", back_populates="menu_items")