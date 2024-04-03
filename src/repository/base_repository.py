from typing import Generic, TypeVar
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert

TModel = TypeVar("TModel")
TCreate = TypeVar("TCreate")

class BaseRepository(Generic[TModel, TCreate]):
    def __init__(self, model: TModel = TModel, model_create: TCreate = TCreate):
        self.model = model
        self.model_create = model_create
        
    async def add(self, db: AsyncSession, obj: TCreate) -> TModel:
        db_obj = self.model(**obj.__dict__)
        db.add(db_obj)
        await db.commit()
        return db_obj
        