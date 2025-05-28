
# Forsit E-commerce Admin API

This is a back-end API built for the Forsit Admin Dashboard, designed to support analytics and inventory management for products sold on platforms like Amazon and Walmart.

---

## 🚀 Tech Stack

- **Language**: Python 3.11+
- **Framework**: FastAPI
- **API Style**: RESTful
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Runtime**: Uvicorn

---

## ⚙️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/Sarim-Soh/Forsit-api.git
cd Forsit-api

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Ensure PostgreSQL is running on port 8181 and update DB URL in app/database.py

# Seed demo data
python -m app.seed

# Start the server
uvicorn app.main:app --reload
```

Swagger UI will be available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📊 API Endpoints

### Sales
- `GET /sales?start=YYYY-MM-DD&end=YYYY-MM-DD`
- `GET /sales/revenue?period=daily|weekly|monthly`
- `GET /sales/by-product?product_id=`

### Inventory
- `GET /inventory`
- `GET /inventory/low-stock?threshold=`
- `PATCH /inventory/{id}?new_stock=`

---

## 🗃️ Database Schema

### `products`
- `id` (PK)
- `name`
- `category`
- `price`

### `sales`
- `id` (PK)
- `product_id` (FK)
- `quantity`
- `total_amount`
- `date`

### `inventory`
- `id` (PK)
- `product_id` (FK)
- `stock_level`
- `last_updated`

---

## 🧪 Demo Data

Run `python -m app.seed` to populate sample data for Amazon and Walmart products and transactions.
