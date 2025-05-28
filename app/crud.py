from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session):
    return db.query(models.Product).all()

def get_sales_by_period(db: Session, start: datetime, end: datetime):
    return db.query(models.Sale).filter(models.Sale.date.between(start, end)).all()

def get_inventory(db: Session):
    return db.query(models.Inventory).all()