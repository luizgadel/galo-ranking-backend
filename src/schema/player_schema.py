from pydantic import BaseModel


class PlayerCreate(BaseModel):
    name: str
    
class Player(PlayerCreate):
    id: int

    class Config:
        orm_mode = True