from sqlalchemy import Column, Integer, ForeignKey

from src.config.config_db import Base

class Galo(Base):
    __tablename__ = "galo"
    
    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey('match.id'), nullable=False)
    team_wr = Column(Integer, ForeignKey('team.id'), nullable=False)