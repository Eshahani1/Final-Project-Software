from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_date = Column(DATETIME, server_default=str(datetime.now()))
    guest_id = Column(Integer, ForeignKey("guests.id"))
    tracking_nums = Column(Integer, unique=True)
    status = Column(String(10))

    card_number = Column(Integer, unique=True)
    pin = Column(Integer)
    method = Column(String(10))
    transaction_status = Column(String(30))

    order_details = relationship("OrderDetail", back_populates="orders")
    guests = relationship("Guest", back_populates="orders")



