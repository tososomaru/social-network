from typing import TypeVar

from pydantic import BaseModel


class BaseSchema(BaseModel):
    pass


class BaseSchemaCreate(BaseModel):
    pass


class BaseSchemaUpdate(BaseModel):
    pass


class BaseSchemaDB(BaseModel):

    class Config:
        from_orm = True


S = TypeVar("S", bound=BaseSchema)
SC = TypeVar("SC", bound=BaseSchemaCreate)
SU = TypeVar("SU", bound=BaseSchemaUpdate)
SD = TypeVar("SD", bound=BaseSchemaDB)
