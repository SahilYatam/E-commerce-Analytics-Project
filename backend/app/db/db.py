import asyncpg
from typing import Optional
from app.core.config import get_settings


class Database:
    def __init__(self):
        self.pool: Optional[asyncpg.Pool] = None

    def _get_pool(self) -> asyncpg.Pool:
        if self.pool is None:
            raise RuntimeError("Database pool is not initialized")
        return self.pool

    async def connect(self):
        settings = get_settings()

        self.pool = await asyncpg.create_pool(
            dsn=settings.DATABASE_URL, min_size=1, max_size=10
        )

    async def disconnect(self):
        if self.pool:
            await self.pool.close()

    async def fetch(self, query: str, *args):
        pool = self._get_pool()
        async with pool.acquire() as conn:
            return await conn.fetch(query, *args)

    async def fetchrow(self, query: str, *args):
        pool = self._get_pool()
        async with pool.acquire() as conn:
            return await conn.fetchrow(query, *args)

    async def execute(self, query: str, *args):
        pool = self._get_pool()
        async with pool.acquire() as conn:
            return await conn.execute(query, *args)


db = Database()
