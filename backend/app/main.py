from fastapi import FastAPI
from app.db.db import db
from app.core.config import get_settings

app = FastAPI()

@app.get("/health")
def health_check():
    return {"Status": "OK"}

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
