from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(18), index=True, nullable=False)
    payment_id = Column(Integer, ForeignKey("payments.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))
    promo_id = Column(Integer, ForeignKey("promos.id"))
    phone_number = Column(String(20), index=True, nullable=False)
    address = Column(String(50), nullable=False)

    payment = relationship("Payment", back_populates="customers")
    order = relationship("Order", back_populates="customers")
    promo = relationship("Promo", back_populates="customers")
