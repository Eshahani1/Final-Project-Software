from sqlalchemy import Column, ForeignKey, Integer, String, Float, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Promo(Base):
    __tablename__ = "promos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(100))
    menu_id = Column(Integer, ForeignKey("menu.id"))
    discount = Column(Float)

    menu_item = relationship("Item", back_populates="promos")