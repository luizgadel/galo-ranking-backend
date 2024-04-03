from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.middleware.utils_db import get_async_session
from src.controller.match_controller import MatchController

match_controller = MatchController()

"""
    @brief      Galo - Sistema de pontuação para Dominó
    
    @details    ...
    
    @author     Luiz Gadelha <>
    @since      Apr 1, 2024
"""

router = APIRouter(tags=["Match"], prefix="/match")

class MatchRoutes:    
    @router.post("/{to_player_one}/{to_player_two}/{tt_player_one}/{tt_player_two}/{team_one_name}/{team_two_name}")
    async def create_match(
        to_player_one: str,
        to_player_two: str,
        tt_player_one: str,
        tt_player_two: str,
        team_one_name: str,
        team_two_name: str,
        db: AsyncSession = Depends(get_async_session)
    ):
        return await match_controller.create_match(
            db, to_player_one, to_player_two, tt_player_one, tt_player_two, team_one_name, team_two_name
        )