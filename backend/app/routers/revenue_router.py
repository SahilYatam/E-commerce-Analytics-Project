from fastapi import APIRouter
from typing import List

from app.schemas.revenue_schema import (
    TotalRevenue,
    TotalOrders,
    AvgOrderValue,
    DailyRevenue,
    MonthlyRevenue,
)

from app.services.revenue_service import (
    get_total_revenue,
    get_total_orders,
    get_avg_order_value,
    get_daily_revenue,
    get_monthly_revenue,
)

router = APIRouter(prefix="/revenue", tags=["Revenue"])


@router.get("/total", response_model=TotalRevenue)
async def total_revenue():
    return await get_total_revenue()


@router.get("/orders/count", response_model=TotalOrders)
async def total_orders():
    return await get_total_orders()


@router.get("/average-order-value", response_model=AvgOrderValue)
async def avg_order_value():
    return await get_avg_order_value()


@router.get("/daily", response_model=List[DailyRevenue])
async def daily_revenue():
    return await get_daily_revenue()


@router.get("/monthly", response_model=List[MonthlyRevenue])
async def monthly_revenue():
    return await get_monthly_revenue()
