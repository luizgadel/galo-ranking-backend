from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.controller.player_controller import PlayerController
from src.repository.team_repository import TeamRepository
from src.schema.team_schema import TeamCreate


class TeamController:
    def __init__(self) -> None:
        self.repository = TeamRepository()
        self.player_controller = PlayerController()
        
    async def get_team_by_player_ids(
        self,
        db: AsyncSession,
        player_one_id: int,
        player_two_id: int
    ):
        db_team = await self.repository.get_team_by_player_ids(db, player_one_id, player_two_id)
        if (db_team):
            return db_team
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Could not find a team with these players.")
        
        
    async def get_team_by_name(self, db: AsyncSession, team_name: str, player_one_name: str, player_two_name: str):
        db_team = await self.repository.get_by_team_name(db, team_name)
        if not db_team:
            db_player_one = await self.player_controller.get_by_name(db, player_one_name)
            db_player_two = await self.player_controller.get_by_name(db, player_two_name)
            team_create = TeamCreate(
                team_name=team_name,
                player_one_id=db_player_one.id,
                player_two_id=db_player_two.id
            )
            db_team = await self.repository.add(db, team_create)
            
        return db_team