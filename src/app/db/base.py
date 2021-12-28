import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy_utils import force_instant_defaults

force_instant_defaults()
from src.app.core.settings import settings

Base: DeclarativeMeta = declarative_base()
database = databases.Database(settings.SQLITE3_URL)

engine = create_engine(
    settings.SQLITE3_URL, connect_args={"check_same_thread": False}
)


