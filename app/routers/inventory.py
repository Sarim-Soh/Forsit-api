from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Inventory
from datetime import datetime

router = APIRouter()

@router.get("/")
def get_inventory(db: Session = Depends(get_db)):
    return db.query(Inventory).all()

@router.get("/low-stock")
def get_low_stock(threshold: int = 10, db: Session = Depends(get_db)):
    return db.query(Inventory).filter(Inventory.stock_level <= threshold).all()

@router.patch("/{inventory_id}")
def update_inventory(inventory_id: int, new_stock: int = Query(...), db: Session = Depends(get_db)):
    item = db.query(Inventory).filter(Inventory.id == inventory_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    item.stock_level = new_stock
    item.last_updated = datetime.utcnow()
    db.commit()
    db.refresh(item)
    return {"status": "updated", "inventory": item}