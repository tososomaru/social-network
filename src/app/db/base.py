import databases
from databases import Database
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from src.app.core.config import get_settings

settings = get_settings()
Base: DeclarativeMeta = declarative_base()
database = databases.Database(url=settings.get_db_url(), min_size=2, max_size=15)


def get_database() -> Database:
    return database
