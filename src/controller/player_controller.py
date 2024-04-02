from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.repository.player_repository import PlayerRepository
from src.schema.player_schema import PlayerCreate

class PlayerController():
    def __init__(self):
        self.repository = PlayerRepository()

    async def new_galo_received(self, db: Session, player_one_name: str, player_two_name: str):
        try:
            db_player_one = await self.get_by_name(db, player_one_name)
            db_player_two = await self.get_by_name(db, player_two_name)

            db_po = await self.repository.new_galo_received(db, db_player_one.id)
            db_pt = await self.repository.new_galo_received(db, db_player_two.id)
            return [db_po, db_pt]
        except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=f'erro: {e}')

    async def new_galo_applied(self, db: Session, player_one_name: str, player_two_name: str):
        db_player_one = await self.get_by_name(db, player_one_name)
        db_player_two = await self.get_by_name(db, player_two_name)

        db_po = await self.repository.new_galo_applied(db, db_player_one.id)
        db_pt = await self.repository.new_galo_applied(db, db_player_two.id)
        return [db_po, db_pt]

    async def add_by_name(self, db: Session, name: str):
        new_player = PlayerCreate(name=name)
        return await self.repository.add(db, new_player)
    
    async def get_by_name(self, db: Session, name: str):
        db_player = await self.repository.get_by_name(db, name)
        
        if (db_player == None):
            await self.add_by_name(db, name)
            return await self.get_by_name(db, name)
        else:
            return db_player