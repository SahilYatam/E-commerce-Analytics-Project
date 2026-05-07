from typing import List
from fastapi import HTTPException
from app.db.db import db
from schemas.products_schema import (
    TopSellingProducts,
    LowStockProducts,
    GetProductByCategory,
    TopCategoryPerMonth,
)

QUERY = """
SELECT
    p.id,
    p.name,
    p.price,
    SUM(oi.quantity) AS total_sold
FROM order_items oi
INNER JOIN orders o
    ON oi.order_id = o.id
INNER JOIN products p
    ON oi.product_id = p.id
WHERE o.order_status = 'completed'
GROUP BY p.id, p.name, p.price
ORDER BY total_sold DESC
LIMIT 10;
"""


async def top_selling_products() -> List[TopSellingProducts]:
    try:
        top_products = await db.fetch(query=QUERY)

        if not top_products:
            return []

        return [
            TopSellingProducts(
                id=top_product["id"],
                name=top_product["name"],
                price=float(top_product["price"]),
                total_sold=top_product["total_sold"],
            )
            for top_product in top_products
        ]
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Failed to fetch top selling products"
        )


QUERY = """
SELECT 
    id,
    name,
    stock_qty,
    price,
    category
FROM products
WHERE stock_qty > 0
    AND stock_qty < $1
ORDER BY stock_qty ASC
LIMIT 50;
"""


async def low_stock_products(threshold: int) -> List[LowStockProducts]:
    try:
        products = await db.fetch(QUERY, threshold)

        if not products:
            return []

        return [
            LowStockProducts(
                id=product["id"],
                name=product["name"],
                stock_qty=product["stock_qty"],
                price=product["price"],
                category=product["category"],
            )
            for product in products
        ]
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Failed to fetch low stock products"
        )


QUERY = """
SELECT 
    id,
    name,
    stock_qty,
    price,
    category
FROM products
WHERE category = $1;
"""


async def get_product_by_category(category: str) -> List[GetProductByCategory]:
    try:
        products = await db.fetchrow(QUERY, category)

        if not products:
            return []

        return [
            GetProductByCategory(
                id=product["id"],
                name=product["name"],
                stock_qty=product["stock_qty"],
                price=product["price"],
                category=product["category"],
            )
            for product in products
        ]
    except Exception:
        raise HTTPException(
            status_code=500, detail="Failed to fetch product by category"
        )


QUERY = """
SELECT month, category, total_revenue
FROM(
    SELECT
        DATE_TRUNC('month', o.created_at) AS month, p.category,
        SUM(oi.quantity * oi.price_at_time) AS total_revenue,
        RANK() OVER(
            PARTITION BY DATE_TRUNC('month', o.created_at)
            ORDER BY SUM(oi.quantity * oi.price_at_time) DESC
        ) AS rank
    FROM order_items oi
    INNER JOIN orders o
        ON oi.order_id = o.id
    INNER JOIN products p
        ON oi.product_id = p.id
    WHERE o.order_status = 'completed'
    GROUP BY month, p.category
) ranked
WHERE rank = 1
ORDER BY month;
"""


async def top_category_per_month() -> List[TopCategoryPerMonth]:
    try:
        top_categories = await db.fetch(QUERY)

        return [
            TopCategoryPerMonth(
                month=top_category["month"],
                category=top_category["category"],
                total_revenue=float(top_category["total_revenue"]),
            )
            for top_category in top_categories
        ]
    except Exception:
        raise HTTPException(
            status_code=500, detail="Failed to fetch top category per month"
        )
