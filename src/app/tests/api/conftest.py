import pytest
from databases import Database
from fastapi_pagination.ext import databases
from sqlalchemy import create_engine

from src.main import app
from src.app.db.base import Base, get_database
from httpx import AsyncClient

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.sqlite3"
# database = Database(TEST_DATABASE_URL, force_rollback=True)

@pytest.fixture(name="database")
def database_fixture():
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    Base.metadata.create_all(bind=engine)
    database = databases.Database(SQLALCHEMY_DATABASE_URL)
    yield database
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(name="client")
def client_fixture(database: Database):
    def get_db_override():
        return database

    app.dependency_overrides[get_database] = get_db_override
    client = AsyncClient(app=app, base_url='http://127.0.0.1:8000')
    yield client
    app.dependency_overrides.clear()
