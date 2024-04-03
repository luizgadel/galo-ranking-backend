from sqlalchemy.ext.asyncio import AsyncSession

from src.controller.player_controller import PlayerController
from src.repository.team_repository import TeamRepository
from src.schema.team_schema import TeamCreate


class TeamController:
    def __init__(self) -> None:
        self.repository = TeamRepository()
        self.player_controller = PlayerController()
        
    async def get_team_by_name(self, db: AsyncSession, team_name: str, player_one_name: str, player_two_name: str):
        db_team = await self.repository.get_by_team_name(db, team_name)
        if not db_team:
            db_player_one = await self.player_controller.get_by_name(db, player_one_name)
            db_player_two = await self.player_controller.get_by_name(db, player_two_name)
            team_create = TeamCreate(
                team_name=team_name,
                player_one=db_player_one.id,
                player_two=db_player_two.id
            )
            db_team = await self.repository.add(db, team_create)
            
        return db_team