from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class PromoDetail(Base):
    __tablename__ = "promo_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    guest_id = Column(Integer, ForeignKey("guests.id"))
    promo_id = Column(Integer, ForeignKey("promos.id"))

    guests = relationship("Guest", back_populates="promo_details")
    promos = relationship("Promo", back_populates="promo_details")
