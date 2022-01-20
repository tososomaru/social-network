import databases
from databases import Database
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from src.app.core.settings import settings

Base: DeclarativeMeta = declarative_base()
database = databases.Database(url=settings.get_db_url(), min_size=2, max_size=15)


def get_database() -> Database:
    return database

# engine = create_async_engine(
#     settings.get_db_url(), connect_args={"check_same_thread": False}
# )
