from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.base_repository import BaseRepository
from src.schema.match_schema import MatchCreate
from src.model.match_model import Match

class MatchRepository(BaseRepository[Match, MatchCreate]):
    def __init__(self):
        super().__init__(Match, MatchCreate)
        
    async def get_open_match(self, db: AsyncSession):
        db_players = await db.scalars(select(self.model).where(self.model.date_time_end == None))
        db_player = db_players.first()
        return db_player