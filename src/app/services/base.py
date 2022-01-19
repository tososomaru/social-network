import abc
from typing import Generic, Type, Optional, TypeVar, List

from databases import Database
from fastapi import HTTPException
from pydantic import UUID4, BaseModel
from starlette import status

from app.app.db.base import Base

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
ModelType = TypeVar("ModelType", bound=Base)

ID = TypeVar('ID', bound=UUID4)


class BaseService(Generic[ModelType, CreateSchemaType, UpdateSchemaType], metaclass=abc.ABCMeta):
    def __init__(self, db: Database, model: Type[ModelType], *args, **kwargs) -> None:
        self.db: Database = db
        self.model = model

    @property
    @abc.abstractmethod
    def _table(self) -> Type[ModelType]:
        return self.model

    async def get_all(self, offset: int, limit: int) -> List[ModelType]:
        return await self.db.fetch_all(query=self.model.select().offset(offset).limit(limit))

    async def get_by_id(self, id: ID) -> Optional[ModelType]:
        return await self.db.fetch_one(query=self.model.select().where(self.model.c.id == id))

    async def create(self, create_schema: CreateSchemaType, **kwargs) -> ID:
        query = self.model.insert(**create_schema, **kwargs)
        return await self.db.execute(query)

    async def update(self, id: ID, update_schema: UpdateSchemaType, ) -> ModelType:
        # db_post = await self.get_by_id(id=id)
        # if not db_post:
        #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        post = self.model.from_orm(db_post)
        for key, value in update_schema.dict(exclude_unset=True).items():
            setattr(post, key, value)
        query = self.model.update().where(self.model.c.id == id).values(**post.dict())
        await self.db.execute(query=query)
        return post

    async def delete(self, id: ID):
        # db_post = await self.get_by_id(id=id)
        # if not db_post:
        #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        query = self.model.delete().where(self.model.c.id == id)
        await self.db.execute(query=query)
        return None
