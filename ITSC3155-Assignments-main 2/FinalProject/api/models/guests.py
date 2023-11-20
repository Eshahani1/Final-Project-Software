from typing import List

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped
from ..dependencies.database import Base

class Guest(Base):
    __tablename__ = "guests"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(18), index=True, nullable=False)
    phone_number = Column(String(20), index=True, nullable=False)
    address = Column(String(50), nullable=False)

    payment = relationship("Payment", back_populates="guests")
    orders = relationship("Order", back_populates="guests")
    promo = relationship("Promo", back_populates="guests")
