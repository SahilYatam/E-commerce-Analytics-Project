from typing import List
from fastapi import HTTPException
from app.db.db import db

from schemas.orders_schema import OrderStatusDistribution, AverageOrderSize, OrderTrend

STATUS_QUERY = """
SELECT 
    order_status,
    COUNT(*) AS total_orders
FROM orders
GROUP BY order_status;
"""


async def get_order_status() -> List[OrderStatusDistribution]:
    try:
        rows = await db.fetch(STATUS_QUERY)

        if not rows:
            return []

        return [
            OrderStatusDistribution(
                order_status=row["order_status"], total_orders=row["total_orders"]
            )
            for row in rows
        ]
    except Exception:
        raise HTTPException(
            status_code=500, detail="Failed to fetch order status distribution"
        )


AVG_QUERY = """
SELECT
    AVG(o.total_item) AS avg_order_size
FROM orders o
WHERE o.order_status = 'completed';
"""


async def get_avg_order_size() -> AverageOrderSize:
    try:
        row = await db.fetchrow(AVG_QUERY)

        if not row or row["avg_order_size"] is None:
            return AverageOrderSize(avg_order_size=0)

        return AverageOrderSize(avg_order_size=(row["avg_order_size"]))

    except Exception:
        raise HTTPException(
            status_code=500, detail="Failed to fetch average order size"
        )


TREND_QUERY = """
SELECT
    DATE_TRUNC('day', o.created_at) AS day,
    COUNT(*) AS total_orders
FROM orders o
WHERE o.order_status = 'completed'
GROUP BY day
ORDER BY day;
"""


async def get_orders_trends() -> List[OrderTrend]:
    try:
        rows = await db.fetch(TREND_QUERY)

        if not rows:
            return []

        return [
            OrderTrend(day=row["day"], total_orders=row["total_orders"]) for row in rows
        ]
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to fetch order trends")
