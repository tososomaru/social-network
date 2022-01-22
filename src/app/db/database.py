import os

import databases
from databases import Database
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from src.app.core.config import get_settings
from src.app.models.user import users
from src.app.schemas.user import UserDB

settings = get_settings()
database = databases.Database(url=settings.get_db_url(), **settings.database_kwargs)


def get_database() -> Database:
    return database


async def get_user_db():
    yield SQLAlchemyUserDatabase(UserDB, get_database(), users)