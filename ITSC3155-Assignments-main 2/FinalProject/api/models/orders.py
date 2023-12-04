from sqlalchemy import Column, ForeignKey, Integer, String, Float, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
from .order_details import OrderDetail


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_date = Column(DATETIME, server_default=str(datetime.now()))
    guest_id = Column(Integer, ForeignKey("guests.id"))
    tracking_nums = Column(Integer, unique=True)
    order_status = Column(String(10))
    total_cost = Column(Float)

    card_number = Column(Integer, unique=True)
    pin = Column(Integer)
    method = Column(String(10))
    transaction_status = Column(String(30))
    order_preference = Column(String(10))

    def calculate_total_cost(self, db):
        order_details = db.query(OrderDetail).filter(OrderDetail.order_id == self.id).all()
        total_cost = sum(detail.get_cost(db) for detail in order_details)
        self.total_cost = total_cost
        db.commit()
        return total_cost

    order_details = relationship("OrderDetail", back_populates="orders")
    guests = relationship("Guest", back_populates="orders")



