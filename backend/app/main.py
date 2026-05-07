from fastapi import FastAPI
from app.db.db import db
from app.core.config import get_settings
from app.routers.user_router import router as user_router
from app.routers.products_router import router as product_router
from app.routers.orders_router import router as order_router
from app.routers.revenue_router import router as revenue_router

app = FastAPI()

@app.get("/health")
def health_check():
    return {"Status": "OK"}

app.include_router(user_router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(revenue_router)

@app.on_event("startup")
async def startup():
    settings = get_settings()
    print("ENV:", settings.ENVIRONMENT)

    await db.connect()
    print("DB Connected")


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
    print("DB Disconnected")


@app.get("/")
async def root():
    return {"message": "API is running"}
