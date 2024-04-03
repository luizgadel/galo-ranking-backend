from datetime import datetime
from pydantic import BaseModel


class MatchCreate(BaseModel):
    team_one: int
    team_two: int
    score_team_one: int = 0
    score_team_two: int = 0
    data_hora: datetime = datetime.now()

class Match(MatchCreate):
    id: int

    class Config:
        orm_mode = True