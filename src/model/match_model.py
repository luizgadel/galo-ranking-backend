from sqlalchemy import Column, Integer, DateTime, ForeignKey, func

from src.config.config_db import Base

class Match(Base):
    __tablename__ = "match"
    
    id = Column(Integer, primary_key=True, index=True)
    team_one_id = Column(Integer, ForeignKey('team.id'), nullable=False)
    team_two_id = Column(Integer, ForeignKey('team.id'), nullable=False)
    score_team_one = Column(Integer, nullable=False, default=0)
    score_team_two = Column(Integer, nullable=False, default=0)
    date_time_start = Column(DateTime, nullable=False, default=func.current_timestamp())
    date_time_end = Column(DateTime, nullable=True)