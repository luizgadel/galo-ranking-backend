from pydantic import BaseModel


class TeamCreate(BaseModel):
    player_one: int
    player_two: int
    team_name: str

class Team(TeamCreate):
    id: int

    class Config:
        orm_mode = True