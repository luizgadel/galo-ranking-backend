from sqlalchemy import Column, Integer, DateTime, ForeignKey, func

from config.config_db import Base

class Match(Base):
    __tablename__ = "match"
    
    id = Column(Integer, primary_key=True, index=True)
    team_one = Column(Integer, ForeignKey('team.id'), nullable=False)
    team_two = Column(Integer, ForeignKey('team.id'), nullable=False)
    score_team_one = Column(Integer, nullable=False, default=0)
    score_team_two = Column(Integer, nullable=False, default=0)
    data_hora = Column(DateTime, nullable=False, default=func.current_timestamp())