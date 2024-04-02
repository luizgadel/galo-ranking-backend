from sqlalchemy import insert, select, update
from sqlalchemy.orm import Session

from src.model.player_model import Player
from schema.player_schema import PlayerCreate


class PlayerRepository():
    def __init__(self):
        self.model = Player

    async def add(self, db: Session, player_create: PlayerCreate):
        db.execute(insert(self.model).values(**player_create.__dict__))
        db.commit()
    
    async def get_by_name(self, db: Session, player_name: str) -> Player:
        db_players = db.scalars(select(self.model).where(self.model.name == player_name))
        db_player = db_players.first()
        return db_player
    
    async def new_galo_received(self, db: Session, player_id):
        db.execute(
            update(self.model)
            .where(self.model.id == player_id)
            .values(galos_received = self.model.galos_received + 1)
        )
        db.commit()
    
    async def new_galo_applied(self, db: Session, player_id):
        db.execute(
            update(self.model)
            .where(self.model.id == player_id)
            .values(galos_applied = self.model.galos_applied + 1)
        )
        db.commit()