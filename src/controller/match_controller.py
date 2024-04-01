from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from middleware.utils_db import get_session
from repository.match_repository import MatchRepository

match_repository = MatchRepository()

class MatchController:
    async def get_matchs(
        self, db: AsyncSession = Depends(get_session)
    ):
        return await match_repository.get_matchs(db)