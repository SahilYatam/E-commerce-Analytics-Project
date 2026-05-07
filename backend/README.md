# E-Commerce Analytics Backend API

A backend analytics system built with FastAPI, PostgreSQL, and raw SQL queries.

This project focuses on analytics and reporting APIs for an e-commerce platform. It provides endpoints for revenue analytics, customer insights, order trends, product analytics, and business metrics.

The project uses:
- FastAPI
- PostgreSQL
- asyncpg
- Raw SQL
- Pydantic

---

# Features

## User Analytics
- Top customers
- Customer lifetime value
- New vs returning users

## Product Analytics
- Top selling products
- Low stock products
- Products by category
- Top category per month

## Order Analytics
- Order status distribution
- Average order size
- Order trends

## Revenue Analytics
- Total revenue
- Total orders
- Average order value
- Daily revenue
- Monthly revenue

---

# Tech Stack

- FastAPI
- PostgreSQL
- asyncpg
- Pydantic
- Python 3.11+

---

# Project Structure

```bash
app/
│
├── main.py
├── db/
├── routers/
├── schemas/
├── services/
├── core/
│
db/
├── schema/
```

---

# Environment Variables

Create a `.env` file in the root directory.

Example:

```env
PORT=8000

DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=password
DB_NAME=analytics

ENVIRONMENT=development

ALLOWED_ORIGINS=["http://localhost:5173","http://127.0.0.1:3000"]

API_PREFIX=/api
DEBUG=True
```

---
# Installation

## 1. Clone Repository

```bash
git clone <your-repo-url>
cd <project-folder>
```

---

## 2. Install uv

Follow the official installation guide:

https://docs.astral.sh/uv/getting-started/installation/

---

## 3. Install Dependencies

```bash
uv sync
```

---

## 4. Run Server

```bash
uv run uvicorn app.main:app --reload
```

---

# Database Setup

## Create PostgreSQL Database

```sql
CREATE DATABASE analytics;
```

---

## Run Schema File

```bash
psql -U postgres -d analytics -f db/schema.sql
```

---

## Seed Database

```bash
psql -U postgres -d analytics -f db/seed.sql
```

---

# Run Server

```bash
uvicorn app.main:app --reload
```

Server runs on:

```bash
http://localhost:8000
```

---

# API Documentation

FastAPI Swagger Docs:

```bash
http://localhost:8000/docs
```

Redoc:

```bash
http://localhost:8000/redoc
```

---

# API Endpoints

# User Analytics

## Get Top Customers

```http
GET /users/top-customers
```

---

## Get Lifetime Value Users

```http
GET /users/lifetime-value-users
```

---

## Get New And Returning Users

```http
GET /users/new-and-returning-users
```

---

# Product Analytics

## Get Top Selling Products

```http
GET /products/top-products
```

---

## Get Low Stock Products

```http
GET /products/low-stock?threshold=10
```

Query Params:
- `threshold` → stock threshold value

---

## Get Products By Category

```http
GET /products/category-product?category=electronics
```

Query Params:
- `category`

Available categories:
- electronics
- clothing
- home_kitchen
- books
- beauty_personal_care
- sports_outdoors
- other

---

## Get Monthly Top Category

```http
GET /products/monthly-top-category
```

---

# Order Analytics

## Get Order Status Distribution

```http
GET /orders/status-distribution
```

---

## Get Average Order Size

```http
GET /orders/average-size
```

---

## Get Orders Trends

```http
GET /orders/trends
```

---

# Revenue Analytics

## Get Total Revenue

```http
GET /revenue/total
```

---

## Get Total Orders

```http
GET /revenue/orders/count
```

---

## Get Average Order Value

```http
GET /revenue/average-order-value
```

---

## Get Daily Revenue

```http
GET /revenue/daily
```

---

## Get Monthly Revenue

```http
GET /revenue/monthly
```

---

# Notes

- This project uses raw SQL queries instead of ORM.
- PostgreSQL is required.
- All analytics endpoints are read-only.
- Swagger docs are available for testing APIs.

---

# Future Improvements

- Docker support
- Authentication & authorization
- Redis caching
- Pagination
- Date range filters
- Unit & integration tests
- CI/CD pipeline

---

# Author

Built for backend analytics and reporting practice using FastAPI and PostgreSQL.