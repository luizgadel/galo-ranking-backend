from datetime import datetime
from typing import Union
from pydantic import BaseModel


class MatchCreate(BaseModel):
    team_one_id: int
    team_two_id: int
    score_team_one: int = 0
    score_team_two: int = 0
    date_time_start: datetime = datetime.now()
    date_time_end: Union[datetime, None] = None
        

class Match(MatchCreate):
    id: int

    class Config:
        orm_mode = True