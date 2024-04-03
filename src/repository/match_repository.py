from src.repository.base_repository import BaseRepository
from src.schema.match_schema import MatchCreate
from src.model.match_model import Match

class MatchRepository(BaseRepository[Match, MatchCreate]):
    def __init__(self):
        super().__init__(Match, MatchCreate)