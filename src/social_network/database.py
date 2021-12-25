from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import settings
from .tables import Base

engine = create_engine(
    settings.database_url,
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
