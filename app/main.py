from fastapi import FastAPI
from app.routers import sales, inventory
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Forsit E-commerce Admin API",
    version="1.0.0"
)

app.include_router(sales.router, prefix="/sales", tags=["Sales"])
app.include_router(inventory.router, prefix="/inventory", tags=["Inventory"])

@app.get("/")
def read_root():
    return {"message": "Forsit E-commerce Admin API is running."}