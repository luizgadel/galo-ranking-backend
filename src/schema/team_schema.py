from pydantic import BaseModel


class TeamCreate(BaseModel):
    player_one_id: int
    player_two_id: int
    team_name: str

class Team(TeamCreate):
    id: int

    class Config:
        orm_mode = True