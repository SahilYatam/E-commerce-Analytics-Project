from pydantic import BaseModel
from datetime import datetime


class TotalRevenue(BaseModel):
    total_revenue: float


class TotalOrders(BaseModel):
    total_orders: int


class AvgOrderValue(BaseModel):
    avg_order_value: float


class DailyRevenue(BaseModel):
    day: datetime
    total_revenue: float


class MonthlyRevenue(BaseModel):
    month: datetime
    total_revenue: float
