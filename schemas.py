from pydantic import BaseModel
from typing import Optional

# ================CAR
class CarBase(BaseModel):
    name: str
    description: str | None = None
    price: int
    image: str


class CarCreate(CarBase):
    brand_id:  Optional[str]

    pass


class Car(CarBase):
    id: int
    brand_id: int

    class Config:
        orm_mode = True

# ================BRAND
class BrandBase(BaseModel):
    name: str
    logo: str
    description: str | None = None

    class Config:
        orm_mode = True


class BrandCreate(BrandBase):
    pass


class Brand(BrandBase):
    id: int
    cars: list[Car] = []

    class Config:
        orm_mode = True
