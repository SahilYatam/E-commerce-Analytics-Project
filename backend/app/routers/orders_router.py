from fastapi import APIRouter
from typing import List

from app.schemas.orders_schema import (
    OrderStatusDistribution,
    AverageOrderSize,
    OrderTrend,
)

from app.services.orders_service import (
    get_order_status,
    get_avg_order_size,
    get_orders_trends,
)

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get(
    "/status-distribution",
    response_model=List[OrderStatusDistribution],
)
async def status_distribution():
    return await get_order_status()


@router.get(
    "/average-size",
    response_model=AverageOrderSize,
)
async def average_size():
    return await get_avg_order_size()


@router.get(
    "/trends",
    response_model=List[OrderTrend],
)
async def orders_trends():
    return await get_orders_trends()
