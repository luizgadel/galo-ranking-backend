from sqlalchemy import and_, or_, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.base_repository import BaseRepository
from src.schema.team_schema import TeamCreate
from src.model.team_model import Team


class TeamRepository(BaseRepository[Team, TeamCreate]):
    def __init__(self):
        super().__init__(Team, TeamCreate)
        
    async def get_team_by_player_ids(
        self,
        db: AsyncSession,
        player_one_id: int,
        player_two_id: int
    ) -> Team:
        return await self.select_first(
            db, 
            select(self.model).where(
                or_(
                    and_(
                        self.model.player_one_id == player_one_id,
                        self.model.player_two_id == player_two_id                        
                    ),
                    and_(
                        self.model.player_one_id == player_two_id,
                        self.model.player_two_id == player_one_id                        
                    )
                )
            )
        )
        
    async def get_by_team_name(self, db: AsyncSession, team_name: str) -> Team:
        return await self.select_first(
            db, 
            select(self.model).where(self.model.name == team_name)
        )
    
    async def update_name(self, db: AsyncSession, team_name: str, team_id: int) -> Team:
        response = await db.execute(
            update(self.model)
            .where(self.model.id == team_id)
            .values({"name": team_name})
        )
        await db.commit()
        return response