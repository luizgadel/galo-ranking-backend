from pydantic import BaseModel


class GaloCreate(BaseModel):
    match_id: int
    team_wr: int

class Galo(GaloCreate):
    id: int

    class Config:
        orm_mode = True