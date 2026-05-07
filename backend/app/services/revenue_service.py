from typing import List
from fastapi import HTTPException
from app.db.db import db
from app.schemas.revenue_schema import (
    TotalRevenue,
    TotalOrders,
    AvgOrderValue,
    DailyRevenue,
    MonthlyRevenue,
)

TOTAL_REVENUE_QUERY = """
SELECT 
    SUM(total_price) AS total_revenue
FROM orders
WHERE status = 'completed'
"""


async def get_total_revenue() -> TotalRevenue:
    try:
        row = await db.fetchrow(TOTAL_REVENUE_QUERY)

        if not row or row["total_revenue"] is None:
            return TotalRevenue(total_revenue=0.0)

        return TotalRevenue(total_revenue=float(row["total_revenue"]))

    except Exception:
        raise HTTPException(status_code=500, detail="Failed to fetch total revenue")


TOTAL_ORDERS_QUERY = """
SELECT COUNT(*) AS total_orders FROM orders
"""


async def get_total_orders() -> TotalOrders:
    try:
        row = await db.fetchrow(TOTAL_ORDERS_QUERY)

        return TotalOrders(total_orders=row["total_orders"])

    except Exception:
        raise HTTPException(status_code=500, detail="Failed to fetch total orders")


AVG_ORDER_VALUE_QUERY = """
SELECT 
    AVG(total_price) AS avg_order_value
FROM orders
"""


async def get_avg_order_value() -> AvgOrderValue:
    try:
        row = await db.fetchrow(AVG_ORDER_VALUE_QUERY)

        if not row or row["avg_order_value"] is None:
            return AvgOrderValue(avg_order_value=0.0)

        return AvgOrderValue(avg_order_value=float(row["avg_order_value"]))

    except Exception:
        raise HTTPException(
            status_code=500, detail="Failed to fetch average order value"
        )


DAILY_REVENUE_QUERY = """
SELECT
    DATE_TRUNC('day', created_at) AS day,
    SUM(total_price) AS Daily-Revenue
FROM orders
WHERE status = 'completed'
GROUP BY day
ORDER BY day;
"""


async def get_daily_revenue() -> List[DailyRevenue]:
    try:
        rows = await db.fetch(DAILY_REVENUE_QUERY)

        if not rows:
            return []

        return [
            DailyRevenue(day=row["day"], total_revenue=float(row["total_revenue"]))
            for row in rows
        ]

    except Exception:
        raise HTTPException(status_code=500, detail="Failed to fetch daily revenue")


MONTHLY_REVENUE_QUERY = """
SELECT
    DATE_TRUNC('month', created_at) AS month,
    SUM(total_price) AS total_revenue
FROM orders
WHERE status = 'completed'
GROUP BY month
ORDER BY month;
"""


async def get_monthly_revenue() -> List[MonthlyRevenue]:
    try:
        rows = await db.fetch(MONTHLY_REVENUE_QUERY)

        if not rows:
            return []

        return [
            MonthlyRevenue(
                month=row["month"], total_revenue=float(row["total_revenue"])
            )
            for row in rows
        ]

    except Exception:
        raise HTTPException(status_code=500, detail="Failed to fetch monthly revenue")
