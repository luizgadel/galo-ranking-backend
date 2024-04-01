from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from middleware.utils_db import get_session
from model.match_model import Match

class MatchRepository:
    def __init__(self):
        self.model = Match
    
    async def get_matchs(
        self, db: AsyncSession = Depends(get_session)
    ):
        return await db.scalars(select(self.model))