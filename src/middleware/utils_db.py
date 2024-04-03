from sqlalchemy.ext.asyncio import AsyncSession

from src.config.config_db import async_session

async def get_async_session() -> AsyncSession:
    """Open the database connection and return a AsyncSession"""
    async with async_session() as session:
        yield session