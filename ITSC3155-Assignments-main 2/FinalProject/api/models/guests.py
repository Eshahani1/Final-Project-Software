from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Guest(Base):
    __tablename__ = "guests"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    payment_id = Column(Integer, ForeignKey("payments.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))
    promo_id = Column(Integer, ForeignKey("promos.id"))
    phone_number = Column(String, index=True, nullable=False)
    address = Column(String, nullable=False)

    payment = relationship("Payment", back_populates="guests")
    order = relationship("Order", back_populates="guests")
    promo = relationship("Promo", back_populates="guests")
