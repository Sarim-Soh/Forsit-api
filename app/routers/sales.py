from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.database import get_db
from app.models import Sale
from sqlalchemy import func

router = APIRouter()

@router.get("/")
def get_sales(start: str, end: str, db: Session = Depends(get_db)):
    start_dt = datetime.fromisoformat(start)
    end_dt = datetime.fromisoformat(end)
    return db.query(Sale).filter(Sale.date.between(start_dt, end_dt)).all()

@router.get("/revenue")
def get_revenue(period: str = Query("daily", enum=["daily", "weekly", "monthly"]), db: Session = Depends(get_db)):
    now = datetime.utcnow()
    if period == "daily":
        start = now - timedelta(days=1)
    elif period == "weekly":
        start = now - timedelta(weeks=1)
    elif period == "monthly":
        start = now - timedelta(days=30)
    revenue = db.query(func.sum(Sale.total_amount)).filter(Sale.date >= start).scalar()
    return {"period": period, "revenue": revenue or 0.0}

@router.get("/by-product")
def get_sales_by_product(product_id: int, db: Session = Depends(get_db)):
    return db.query(Sale).filter(Sale.product_id == product_id).all()