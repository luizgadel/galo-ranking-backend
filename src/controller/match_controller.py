from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.match_repository import MatchRepository
from src.controller.team_controller import TeamController
from src.schema.match_schema import MatchCreate

match_repository = MatchRepository()

class MatchController:
    def __init__(self):
        self.team_controller = TeamController()
        self.repository = MatchRepository()
    
    async def create_match(
        self, 
        db: AsyncSession,
        to_player_one: str,
        to_player_two: str,
        tt_player_one: str,
        tt_player_two: str,
        team_one_name: str,
        team_two_name: str,
    ):
        team_one = await self.team_controller.get_team_by_name(db, team_one_name, to_player_one, to_player_two)  
        team_two = await self.team_controller.get_team_by_name(db, team_two_name, tt_player_one, tt_player_two)
        
        match_create = MatchCreate(
            team_one=team_one.id,
            team_two=team_two.id
        )
        return await self.repository.add(db, match_create)