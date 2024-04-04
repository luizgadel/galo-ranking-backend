from sqlalchemy import Column, Integer, String, ForeignKey

from src.config.config_db import Base

class Team(Base):
    __tablename__ = "team"
    
    id = Column(Integer, primary_key=True, index=True)
    player_one_id = Column(Integer, ForeignKey('player.id'), nullable=False)
    player_two_id = Column(Integer, ForeignKey('player.id'), nullable=False)
    team_name = Column(String(50), nullable=False)