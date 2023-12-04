from sqlalchemy import Column, ForeignKey, Integer, String, Float, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Promo(Base):
    __tablename__ = "promos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(50), primary_key=True, index=True)
    discount = Column(Float)
    expiration_date = Column(DATETIME, nullable=False)
    

    promo_details = relationship("PromoDetail", back_populates="promos")
