from datetime import datetime
from typing import TypeVar
from uuid import UUID

from pydantic import BaseModel, Field

from src.app.schemas.utils import create_uuid_without_leading_zeros


class BaseSchema(BaseModel):
    pass


class BaseSchemaCreate(BaseModel):
    pass


class BaseSchemaUpdate(BaseModel):
    pass


class BaseSchemaDB(BaseModel):

    class Config:
        from_orm = True


class IdSchemaMixin(BaseModel):
    id: UUID = Field(default_factory=create_uuid_without_leading_zeros, metadata=dict(title='id'))


class TimeStampSchemaMixin(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


S = TypeVar("S", bound=BaseSchema)
SC = TypeVar("SC", bound=BaseSchemaCreate)
SU = TypeVar("SU", bound=BaseSchemaUpdate)
SD = TypeVar("SD", bound=BaseSchemaDB)
