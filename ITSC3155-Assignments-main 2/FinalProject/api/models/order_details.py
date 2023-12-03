from sqlalchemy import Column, ForeignKey, Integer, String, Float, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"))
    amount = Column(Integer, index=True, nullable=False)
    rating_score = Column(Integer, index=True, nullable=True)
    rating_review = Column(String(200), index=True, nullable=True)
    cost = Column(Float)

    menu_items = relationship("MenuItem", back_populates="order_details")
    orders = relationship("Order", back_populates="order_details")
