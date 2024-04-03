from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.base_repository import BaseRepository
from src.schema.player_schema import PlayerCreate
from src.model.player_model import Player


class PlayerRepository(BaseRepository[Player, PlayerCreate]):
    def __init__(self):
        super().__init__(Player, PlayerCreate)
    
    async def get_by_name(self, db: AsyncSession, player_name: str) -> Player:
        db_players = await db.scalars(select(self.model).where(self.model.name == player_name))
        db_player = db_players.first()
        return db_player