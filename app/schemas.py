from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    name: str
    category: str
    price: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True

class SaleBase(BaseModel):
    product_id: int
    quantity: int
    total_amount: float
    date: Optional[datetime] = None

class Sale(SaleBase):
    id: int
    class Config:
        from_attributes = True

class InventoryBase(BaseModel):
    product_id: int
    stock_level: int

class Inventory(InventoryBase):
    id: int
    last_updated: datetime

    class Config:
        from_attributes = True