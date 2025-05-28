from app.database import SessionLocal, engine
from app.models import Base, Product, Inventory, Sale
from datetime import datetime, timedelta

Base.metadata.create_all(bind=engine)
db = SessionLocal()

db.query(Sale).delete()
db.query(Inventory).delete()
db.query(Product).delete()
db.commit()

products = [
    Product(name="Echo Dot (5th Gen)", category="Electronics", price=49.99),  # Amazon
    Product(name="Great Value Notebook", category="Stationery", price=1.25),  # Walmart
    Product(name="Instant Pot Duo 7-in-1", category="Home & Kitchen", price=89.00),  # Amazon
    Product(name="Ozark Trail Water Bottle", category="Outdoors", price=12.97),  # Walmart
]

db.add_all(products)
db.commit()
for product in products:
    db.refresh(product)

# Step 3: Add inventory
inventory_items = [
    Inventory(product_id=products[0].id, stock_level=40),
    Inventory(product_id=products[1].id, stock_level=500),
    Inventory(product_id=products[2].id, stock_level=20),
    Inventory(product_id=products[3].id, stock_level=75),
]
db.add_all(inventory_items)

# Step 4: Add sample sales
today = datetime.now()
sales_entries = [
    Sale(product_id=products[0].id, quantity=10, total_amount=499.90, date=today - timedelta(days=1)),
    Sale(product_id=products[1].id, quantity=50, total_amount=62.50, date=today - timedelta(days=3)),
    Sale(product_id=products[2].id, quantity=5, total_amount=445.00, date=today - timedelta(days=2)),
    Sale(product_id=products[3].id, quantity=15, total_amount=194.55, date=today - timedelta(days=4)),
]
db.add_all(sales_entries)
db.commit()

print("✅ Seeded database with demo data from Amazon & Walmart.")