from pydantic import BaseModel

class TopCustomer(BaseModel):
    id: int
    name: str
    total_spent: float


class LifetimeValueUsers(BaseModel):
    id: int
    name: str
    lifetime_value: float


class NewAndReturningUsers(BaseModel):
    new_users: int
    returning_users: int
