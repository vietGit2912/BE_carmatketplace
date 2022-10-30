from fastapi import Depends, FastAPI, HTTPException, status, Response
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import crud
import models
import schemas
import database

# API instance
app = FastAPI()

# Origin
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Enable binding
models.Base.metadata.create_all(bind=database.engine)


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -========================BRAND
# CREATE BRAND
@app.post("/brand", status_code=status.HTTP_201_CREATED)
def create_brand(brand: schemas.BrandCreate, db: Session = Depends(get_db)):
    if crud.is_brand_exist(db, brand.name):
        return Response(status_code=status.HTTP_409_CONFLICT, content="Cannot create because brand is exist")
    crud.create_brand(db, brand)


# GET ALL BRAND
@app.get("/brands", response_model=list[schemas.Brand], status_code=status.HTTP_200_OK)
def get_brands(db: Session = Depends(get_db)):
    return crud.get_brands(db)


# GET BRAND DETAIL
@app.get("/brand/{brand_name}", response_model=schemas.Brand)
def get_brand_detail(brand_name: str, db: Session = Depends(get_db)):
    # let framework auto raise error for sqlalchemy ==> default 500
    db_brand = crud.get_brand(db, brand_name)
    if db_brand is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Brand not found")
    return db_brand


# UPDATE BRAND
@app.patch("/brand/{brand_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_brand(brand_id: str, brand: schemas.BrandCreate, db: Session = Depends(get_db)):
    db_brand = crud.get_brand(db, brand_id)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")

    brand_data = brand.dict(exclude_unset=True)
    for key, value in brand_data.items():
        setattr(db_brand, key, value)

    crud.update_brand(db, db_brand)


# DELETE ALL BRAND
@app.delete("/delete_brands", status_code=status.HTTP_204_NO_CONTENT)
def delete_brands(db: Session = Depends(get_db)):
    crud.delete_all_brand(db)


# DELETE BRAND
@app.delete("/brand/{brand_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_brand(brand_id: int, db: Session = Depends(get_db)):
    crud.delete_brand(db, brand_id)


# -========================CAR
# FAKE CAR


@app.get("/cars/addAll", status_code=status.HTTP_200_OK)
def add_dumb_car_data(db: Session = Depends(get_db)):
    try:
        crud.create_dumb(db)
    except:
        raise HTTPException(status_code=500, detail="Cannot create dumb data")


@app.get("/brands/addAll", status_code=status.HTTP_200_OK)
def add_dumb_brand_data(db: Session = Depends(get_db)):
    return crud.create_dumb_brand(db)


# CREATE CAR
@app.post("/cars/", status_code=status.HTTP_201_CREATED)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    if crud.create_car(db, car):
        return crud.create_car(db, car)
    raise HTTPException(status_code=500, detail="Server cannot process request")


# GET ALL CAR
@app.get("/cars/", response_model=list[schemas.Car])
def get_cars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_cars(db, skip=skip, limit=limit)
    return items


# GET CAR DETAIL
@app.get("/car/{car_id}", response_model=schemas.Car)
def get_car_detail(car_id: int, db: Session = Depends(get_db)):
    db_car = crud.get_car(db, car_id=car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car


# UPDATE CAR
@app.patch("/car/{car_id}", response_model=schemas.Car)
def update_car(car_id: str, car: schemas.CarCreate, db: Session = Depends(get_db)):
    db_car = crud.get_car(db, car_id)
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    car_data = car.dict(exclude_unset=True)
    for key, value in car_data.items():
        setattr(db_car, key, value)
    crud.update_car(db, db_car)
    return db_car


# DELETE CAR
@app.delete("/car/{car_id}")
def delete_car(car_id: int, db: Session = Depends(get_db)):
    car = crud.get_car(db, car_id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    crud.delete_car(db, car)
    return {"ok": True}


# GET ALL CARD BY BRAND NAME
@app.get("/{brand_name}/cars", response_model=list[schemas.Car])
def get_all_car_by_brand(brand_name: str, db: Session = Depends(get_db)):
    return crud.get_cars_by_brand(db, brand_name)


# SEARCH CAR BY KEYWORD

@app.get("/searchcar/{keyword}", response_model=list[schemas.Car])
def search_cars_by_keyword(keyword: str, db: Session = Depends(get_db)):
    return crud.search_cars_by_keyword(db, keyword)
