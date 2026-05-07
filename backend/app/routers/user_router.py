from fastapi import APIRouter
from typing import List

from app.schemas.user_schema import (
    TopCustomer,
    LifetimeValueUsers,
    NewAndReturningUsers,
)

from app.services.user_service import (
    get_top_customers,
    get_lifetime_value_users,
    get_new_and_returning_users,
)

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/top-customers", response_model=List[TopCustomer])
async def top_customers():
    return await get_top_customers()


@router.get("/lifetime-value-users", response_model=List[LifetimeValueUsers])
async def lifetime_value_users():
    return await get_lifetime_value_users()


@router.get("/new-and-returning-users", response_model=[NewAndReturningUsers])
async def new_and_returning_users():
    return await get_new_and_returning_users()
