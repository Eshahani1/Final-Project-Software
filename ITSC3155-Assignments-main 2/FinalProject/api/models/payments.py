from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    number = Column(Integer, unique=True, nullable=False)
    pin = Column(Integer, unique=True, nullable=True)
    type = Column(String(255), nullable=False)

    guests = relationship("Guest", back_populates="payment")