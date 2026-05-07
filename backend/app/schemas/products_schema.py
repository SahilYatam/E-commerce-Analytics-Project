from pydantic import BaseModel
from datetime import datetime


class TopSellingProducts(BaseModel):
    id: int
    name: str
    price: float
    total_sold: int


class LowStockProducts(BaseModel):
    id: int
    name: str
    stock_qty: int
    price: float
    category: str


class GetProductByCategory(BaseModel):
    id: int
    name: str
    stock_qty: int
    price: float
    category: str


class TopCategoryPerMonth(BaseModel):
    month: datetime
    category: str
    total_revenue: float
    

