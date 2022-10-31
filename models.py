from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from typing import Optional, List
from database import Base
from schemas import Car


#======FOR REAL

class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    logo = Column(String)
    description = Column(String)

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer, index=True)
    image = Column(String, index=True)

    brand_id = Column(Integer, ForeignKey("brands.id"))







