from sqlalchemy import Column, Integer, String

from src.config.config_db import Base

class Player(Base):
    __tablename__ = "player"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)