from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.app.core.settings import settings
from src.app.db.base import Base

engine = create_engine(
    settings.SQLITE3_URL,
    connect_args={'check_same_thread': False}
)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False
)


def migration_db() -> None:
    Base.metadata.create_all(engine)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()
