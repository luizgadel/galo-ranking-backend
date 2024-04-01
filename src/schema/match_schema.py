from datetime import datetime
from pydantic import BaseModel


class MatchCreate(BaseModel):
    team_one: int
    team_two: int
    score_team_one: int
    score_team_two: int
    data_hora: datetime

class Match(MatchCreate):
    id: int

    class Config:
        orm_mode = True