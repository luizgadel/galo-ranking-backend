from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.middleware.utils_db import get_async_session
from src.controller.player_controller import PlayerController
from src.schema.player_schema import PlayerCreate

player_controller = PlayerController()

"""
    @brief      Galo - Sistema de pontuação para Dominó
    
    @details    ...
    
    @author     Luiz Gadelha <>
    @since      Apr 1, 2024
"""

router = APIRouter(tags=["Player"], prefix="/player")

class PlayerRoutes:
    pass
    