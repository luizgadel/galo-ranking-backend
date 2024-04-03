from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.base_repository import BaseRepository
from src.schema.team_schema import TeamCreate
from src.model.team_model import Team


class TeamRepository(BaseRepository[Team, TeamCreate]):
    def __init__(self):
        super().__init__(Team, TeamCreate)
        
    async def get_by_team_name(self, db: AsyncSession, team_name: str) -> Team:
        db_teams = await db.scalars(select(self.model).where(self.model.team_name == team_name))
        db_team = db_teams.first()
        return db_team