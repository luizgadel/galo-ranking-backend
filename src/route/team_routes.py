from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.middleware.utils_db import get_async_session
from src.controller.team_controller import TeamController

team_controller = TeamController()

"""
    @brief      Galo - Sistema de pontuação para Dominó
    
    @details    ...
    
    @author     Luiz Gadelha <>
    @since      Apr 4, 2024
"""

router = APIRouter(tags=["Team"], prefix="/team")

class TeamRoutes:
    @router.get("/{player_one_id}/{player_two_id}")
    async def get_team_by_player_ids(
        player_one_id: int,
        player_two_id: int,
        db: AsyncSession = Depends(get_async_session)
    ):
        return await team_controller.get_team_by_player_ids(db, player_one_id, player_two_id)