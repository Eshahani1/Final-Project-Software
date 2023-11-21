from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    guest_id = Column(Integer, ForeignKey("guests.id"))
    card_number = Column(Integer, unique=True, nullable=False)
    pin = Column(Integer, unique=True, nullable=True)
    method = Column(String(5), nullable=False)

    guests = relationship("Guest", back_populates="payments")

