from fastapi import HTTPException, status
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
        if (await self.is_there_an_open_match(db)):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, 
                detail="Cannot create a new match since there is an ongoing one."
            )
        else:
            team_one = await self.team_controller.persist_team(db, team_one_name, to_player_one, to_player_two)  
            team_two = await self.team_controller.persist_team(db, team_two_name, tt_player_one, tt_player_two)
            
            match_create = MatchCreate(
                team_one_id=team_one.id,
                team_two_id=team_two.id
            )
            return await self.repository.add(db, match_create)
    
    async def is_there_an_open_match(self, db: AsyncSession) -> bool:
        db_match = await self.repository.get_open_match(db)
        return (db_match != None)