from sqlalchemy import Column, ForeignKey, Integer, String, Float, DECIMAL, DATETIME, Float, event
from sqlalchemy.orm import relationship
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_date = Column(DATETIME, server_default=str(datetime.now()))
    guest_id = Column(Integer, ForeignKey("guests.id"))
    promo_code = Column(String(50),nullable=True)
    discount_code = Column(Float, nullable=True)  
    tracking_nums = Column(Integer, unique=True)
    order_status = Column(String(10))
    card_number = Column(Integer)
    pin = Column(Integer)
    method = Column(String(10))
    transaction_status = Column(String(30))
    order_preference = Column(String(10))
    total_cost = Column(Float)

    order_details = relationship("OrderDetail", back_populates="orders")
    guests = relationship("Guest", back_populates="orders")
    