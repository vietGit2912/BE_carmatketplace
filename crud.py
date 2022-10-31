from sqlalchemy.orm import Session

import models
import schemas

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
        name="Audi A8",
        description="Audi A8",
        price=120000,
        image="https://giaxeoto.vn/admin/upload/images/resize/640-than-xe-audi-a8-2018-2019.jpg",
        brand_id=2
    )
    car3 = schemas.CarCreate(
        name="Audi R10",
        description="Audi R10",
        price=80000,
        image="https://img.tinxe.vn/2020/07/07/8EVDUW1z/gia-xe-audi-r8-mau-do-cb85.jpg",
        brand_id=2
    )
    car4 = schemas.CarCreate(
        name="BMW Model 2022",
        description="BMW here",
        price=75000,
        image="https://imgd.aeplcdn.com/0x0/n/cw/ec/41406/bmw-8-series-right-front-three-quarter8.jpeg",
        brand_id=1
    )
    car5 = schemas.CarCreate(
        name="Lexus RX",
        description="BMW here",
        price=120000,
        image="https://media.vov.vn/sites/default/files/styles/large/public/2022-06/2023-lexus-rx-10.jpg",
        brand_id=6
    )
    car6 = schemas.CarCreate(
        name="Postche SC123",
        description="Postche Brand",
        price=80000,
        image="https://cars.usnews.com/static/images/Auto/izmo/i159615142/2023_porsche_macan_angularfront.jpg",
        brand_id=7
    )
    car7 = schemas.CarCreate(
        name="Lamborghini Avendator LP780",
        description="Lamborghini Avendator LP780",
        price=200000,
        image="https://vcdn1-vnexpress.vnecdn.net/2021/07/07/Aventador-Ultimae-Coupe-1-3961-1625659942.jpg?w=680&h=0&q=100&dpr=1&fit=crop&s=-bQfhP52fmZis8gCgeHLoQ",
        brand_id=4
    )
    car8 = schemas.CarCreate(
        name="Lamborghini SC18",
        description="Lamborghini SC18",
        price=200000,
        image="https://cms-i.autodaily.vn/du-lieu/2018/11/18/lamborghini-sc18-7.jpg",
        brand_id=4
    )
    car9 = schemas.CarCreate(
        name="Lamborghini Spec",
        description="Lamborghini Spec",
        price=240000,
        image="https://m.atcdn.co.uk/vms/media/4c06bec9fcd34fc89102eee8f4128dc6.jpg",
        brand_id=4
    )

    car10 = schemas.CarCreate(
        name="Mazda",
        description="Mazda",
        price=70000,
        image="https://mazdamotors.vn/media/z3cfgn1a/1.jpg",
        brand_id=3
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
    db_car = models.Car(**car8.dict())
    db.add(db_car)
    db_car = models.Car(**car9.dict())
    db.add(db_car)
    db_car = models.Car(**car10.dict())
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
        logo="https://www.pikpng.com/pngl/m/17-173029_audi-logo-png-transparent-svg-vector-freebie-supply.png"
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
    brand7 = schemas.BrandCreate(
        name="Porsche",
        description="Porsche Brand",
        logo="https://png.monster/wp-content/uploads/2022/02/png.monster-758-370x370.png"
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

    db_brand = models.Brand(**brand7.dict())
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


def delete_all_car(db: Session):
    db.query(models.Car).delete()
    db.commit()


def get_cars_by_brand(db: Session, brand_name: str):
    db_brand = db.query(models.Brand).filter(models.Brand.name == brand_name).first()
    brand_id = db_brand.id
    return db.query(models.Car).filter(models.Car.brand_id == brand_id).all()


def get_cars_by_keyword(db: Session, brand_name: str, keyword: str):
    db_brand = db.query(models.Brand).filter(models.Brand.name == brand_name).first()
    brand_id = db_brand.id
    return db.query(models.Car).filter(models.Car.brand_id == brand_id, models.Car.name.contains(keyword)).all()


# =======BRAND
def get_brands(db: Session):
    return db.query(models.Brand).all()


def get_brand(db: Session, brand_name: str):
    return db.query(models.Brand).filter(models.Brand.name == brand_name).first()


def get_brand_by_id(db: Session, brand_id: int):
    return db.query(models.Brand).filter(models.Brand.id == brand_id).first()


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


def delete_brand_by_id(db: Session, brand_id: int):
    try:
        db_brand = get_brand_by_id(db, brand_id)
        db.delete(db_brand)
        db.commit()
    except:
        db.rollback()
