from fastapi import APIRouter
from typing import List

from app.schemas.products_schema import (
    TopSellingProducts,
    LowStockProducts,
    GetProductByCategory,
    TopCategoryPerMonth,
)

from app.services.products_service import (
    top_selling_products,
    low_stock_products,
    get_product_by_category,
    top_category_per_month,
)

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/top-products", response_model=List[TopSellingProducts])
async def top_products():
    return await top_selling_products()


@router.get("/low-stock", response_model=List[LowStockProducts])
async def low_stock(threshold: int = 10):
    return await low_stock_products(threshold)


@router.get("/category-product", response_model=List[GetProductByCategory])
async def category_product(category: str):
    return await get_product_by_category(category)


@router.get("/monthly-top-category", response_model=List[TopCategoryPerMonth])
async def monthly_top_category():
    return await top_category_per_month()
