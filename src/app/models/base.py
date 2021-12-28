# import uuid
# from typing import TypeVar
#
# import sqlalchemy as sa
# from fastapi_users_db_sqlalchemy import GUID
# from sqlalchemy.ext.declarative import as_declarative, declared_attr
#
#
# @as_declarative()
# class Base:
#     id: uuid.UUID = sa.Column(GUID, primary_key=True)
#     __name__: str
#
#     @declared_attr
#     def __tablename__(cls) -> str:
#         return cls.__name__.lower()
