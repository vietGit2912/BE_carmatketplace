from sqlalchemy.orm import Session

import models, schemas
from dataoperation import LambdaFunction
from sqlalchemy.exc import DontWrapMixin

class MyCustomException(Exception, DontWrapMixin):
    pass

# ========CRUD CAR
def create_dumb(db: Session):
    car1 = schemas.CarCreate(
        name="BMW i8",
        description="BMW here",
        price=80000,
        image="https://www.bmw.vn/content/dam/bmw/common/all-models/z-series/roadster/2021/navigation/bmw-zseries-z4-firstedition-modellfinder.png",
        brand_id=1
    )
    car2 = schemas.CarCreate(
        name="BMW i8",
        description="BMW here",
        price=80000,
        image="https://www.bmw.vn/content/dam/bmw/common/all-models/z-series/roadster/2021/navigation/bmw-zseries-z4-firstedition-modellfinder.png",
        brand_id=2
    )
    car3 = schemas.CarCreate(
        name="BMW i8",
        description="BMW here",
        price=80000,
        image="https://www.bmw.vn/content/dam/bmw/common/all-models/z-series/roadster/2021/navigation/bmw-zseries-z4-firstedition-modellfinder.png",
        brand_id=2
    )
    car4 = schemas.CarCreate(
        name="BMW i8",
        description="BMW here",
        price=80000,
        image="https://www.bmw.vn/content/dam/bmw/common/all-models/z-series/roadster/2021/navigation/bmw-zseries-z4-firstedition-modellfinder.png",
        brand_id=1
    )
    car5 = schemas.CarCreate(
        name="BMW i8",
        description="BMW here",
        price=80000,
        image="https://www.bmw.vn/content/dam/bmw/common/all-models/z-series/roadster/2021/navigation/bmw-zseries-z4-firstedition-modellfinder.png",
        brand_id=2
    )
    car6 = schemas.CarCreate(
        name="BMW i8",
        description="BMW here",
        price=80000,
        image="https://www.bmw.vn/content/dam/bmw/common/all-models/z-series/roadster/2021/navigation/bmw-zseries-z4"
              "-firstedition-modellfinder.png",
        brand_id=2
    )
    car7 = schemas.CarCreate(
        name="BMW i8",
        description="BMW here",
        price=80000,
        image="https://www.bmw.vn/content/dam/bmw/common/all-models/z-series/roadster/2021/navigation/bmw-zseries-z4"
              "-firstedition-modellfinder.png",
        brand_id=1
    )

    db_car = models.Car(**car1.dict())
    db.add(db_car)
    db_car = models.Car(**car2.dict())
    db.add(db_car)
    db_car = models.Car(**car3.dict())
    db.add(db_car)
    db_car = models.Car(**car4.dict())
    db.add(db_car)
    db_car = models.Car(**car5.dict())
    db.add(db_car)
    db_car = models.Car(**car6.dict())
    db.add(db_car)
    db_car = models.Car(**car7.dict())
    db.add(db_car)
    db.commit()


def create_dumb_brand(db: Session):
    brand1 = schemas.BrandCreate(
        name="BMW",
        description="BMW Brand",
        logo="https://brademar.com/wp-content/uploads/2022/05/BMW-Logo-PNG-1.png"
    )
    brand2 = schemas.BrandCreate(
        name="Audi",
        description="Audi Brand",
        logo="https://vudigital.co/wp-content/uploads/2021/09/logo-audi-bieu-tuong-thuong-hieu-xe-hoi-thay-doi-nhieu-nhat-ke-tu-1909-12.jpg"
    )
    brand3 = schemas.BrandCreate(
        name="Mazda",
        description="Mazda Brand",
        logo="https://brademar.com/wp-content/uploads/2022/05/Mazda-Logo-PNG-3.png"
    )
    brand4 = schemas.BrandCreate(
        name="Lamborghini",
        description="Lamborghini Brand",
        logo="https://logos-world.net/wp-content/uploads/2021/03/Lamborghini-Logo.png"
    )
    brand5 = schemas.BrandCreate(
        name="Ferrari",
        description="Ferrari Brand",
        logo="https://logoxe.net/wp-content/uploads/2021/07/logo-xe-ferrari.jpg"
    )
    brand6 = schemas.BrandCreate(
        name="Lexus",
        description="Lexus Brand",
        logo="https://1000logos.net/wp-content/uploads/2021/04/Lexus-Logo.png"
    )

    db_brand = models.Brand(**brand1.dict())
    db.add(db_brand)

    db_brand = models.Brand(**brand2.dict())
    db.add(db_brand)

    db_brand = models.Brand(**brand3.dict())
    db.add(db_brand)

    db_brand = models.Brand(**brand4.dict())
    db.add(db_brand)

    db_brand = models.Brand(**brand5.dict())
    db.add(db_brand)

    db_brand = models.Brand(**brand6.dict())
    db.add(db_brand)

    db.commit()


def get_cars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Car).offset(skip).limit(limit).all()


def get_car(db: Session, car_id: int):
    db_row = db.query(models.Car).filter(models.Car.id == car_id).first()
    return db_row


def create_car(db: Session, car: schemas.CarCreate):
    try:
        db_car = models.Car(**car.dict())
        db.add(db_car)
        db.commit()
        db.refresh(db_car)
        return True
    except:
        db.rollback()
        return False


def update_car(db: Session, car: schemas.CarCreate):
    db.add(car)
    db.commit()
    db.refresh(car)


def delete_car(db: Session, car: schemas.CarCreate):
    db.delete(car)
    db.commit()


def get_cars_by_brand(db: Session, brand_name: str):
    return db.query(models.Car).filter(models.Car.brand_name == brand_name).all()


def search_cars_by_keyword(db: Session, keyword: str):
    rs = LambdaFunction.search_by_price_contain()
    rs(keyword)
    return db.query(models.Car).filter(rs(keyword)).all()


# =======BRAND
def get_brands(db: Session):
    return db.query(models.Brand).all()


def get_brand(db: Session, brand_name: str):
    return db.query(models.Brand).filter(models.Brand.name == brand_name).first()


def is_brand_exist(db: Session, brand_name: str):
    brand = db.query(models.Brand).filter(models.Brand.name == brand_name).first()
    if brand:
        return True
    return False


def create_brand(db: Session, brand: schemas.BrandCreate):
    db_brand = models.Brand(**brand.dict())
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand


def update_brand(db: Session, brand: schemas.BrandCreate):
    db.add(brand)
    db.commit()
    db.refresh(brand)


def delete_all_brand(db: Session):
    db.query(models.Brand).delete()
    db.commit()


def delete_brand(db: Session, brand_id: int):
    try:
        db_brand = get_brand(db, brand_id)
        db.delete(db_brand)
        db.commit()
        print("done delete car")
    except:
        db.rollback()
