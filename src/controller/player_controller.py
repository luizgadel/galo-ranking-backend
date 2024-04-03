from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.player_repository import PlayerRepository
from src.schema.player_schema import PlayerCreate

class PlayerController():
    def __init__(self):
        self.repository = PlayerRepository()

    async def add_by_name(self, db: AsyncSession, name: str):
        new_player = PlayerCreate(name=name)
        return await self.repository.add(db, new_player)
    
    async def get_by_name(self, db: AsyncSession, name: str):
        db_player = await self.repository.get_by_name(db, name)
        
        if not db_player:
            await self.add_by_name(db, name)
            return await self.get_by_name(db, name)
        else:
            return db_player