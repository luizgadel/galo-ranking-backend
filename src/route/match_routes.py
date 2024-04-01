from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from middleware.utils_db import get_session
from controller.match_controller import MatchController

match_controller = MatchController()

"""
    @brief      Galo - Sistema de pontuação para Dominó
    
    @details    Main file. Instance the FastAPI and include main endpoints of application
    
    @author     Luiz Gadelha <>
    @since      Mar 1, 2024
"""

router = APIRouter(tags=["Match"], prefix="/match")

class MatchRoutes:
    @router.get("/")
    async def get_matchs(
        self, db: AsyncSession = Depends(get_session)
    ):
        return await match_controller.get_matchs(db)