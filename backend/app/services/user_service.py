from typing import List
from fastapi import HTTPException
from app.db.db import db
from schemas.user_schema import TopCustomer, LifetimeValueUsers, NewAndReturningUsers

QUERY = """
SELECT 
    u.id,
    u.name,
    SUM(o.total_price) AS total_spent
FROM orders o
INNER JOIN users u
    ON o.user_id = u.id
WHERE o.order_status = 'completed'
GROUP BY u.id, u.name
ORDER BY total_spent DESC
LIMIT 10;
"""

async def get_top_customers() -> List[TopCustomer]:
    try:
        rows = await db.fetch(query=QUERY)

        if not rows:
            return []

        return [
            TopCustomer(
                id=row["id"],
                name=row["name"],
                total_spent=float(row["total_spent"]),
            )
            for row in rows
        ]
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Failed to fetch top customers"
        )

QUERY="""
SELECT 
    u.id,
    u.name,
    SUM(o.total_price) AS lifetime_value
FROM orders o
INNER JOIN users u
    ON o.user_id = u.id
WHERE o.order_status = 'completed'
GROUP BY u.id, u.name;
"""

async def get_lifetime_value_users() -> List[LifetimeValueUsers]:
    try:
        users = await db.fetch(query=QUERY)
        
        if not users:
            return[]
        
        return[
            LifetimeValueUsers(
                id=user["id"],
                name=user["name"],
                lifetime_value=float(user["lifetime_value"]),
            )
            for user in users
        ]
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Failed to fetch lifetime value users"
        )


QUERY="""
SELECT
    COUNT(CASE WHEN order_count = 1 THEN 1 END) AS new_users,
    COUNT(CASE WHEN order_count > 1 THEN 1 END) AS returning_users
FROM (
    SELECT
        user_id,
        COUNT(*) AS order_count
    FROM orders
    WHERE order_status = 'completed'
    GROUP BY user_id
) AS user_orders;

"""

async def get_new_and_returning_users() -> NewAndReturningUsers:
    try:
        row = await db.fetchrow(query=QUERY)
        
        if not row:
            return NewAndReturningUsers(
                new_users=0,
                returning_users=0
            )
        
        return NewAndReturningUsers(
                new_users=row["new_users"],
                returning_users=row["returning_users"]
            )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Failed to fetch New And Returning users"
        )



