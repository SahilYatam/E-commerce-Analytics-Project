from pydantic import BaseModel
from datetime import datetime


class OrderStatusDistribution(BaseModel):
    order_status: str
    total_orders: int


class AverageOrderSize(BaseModel):
    avg_order_size: float


class OrderTrend(BaseModel):
    day: datetime
    total_orders: int
