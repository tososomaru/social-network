import os
import pytest
from databases import Database
from fastapi import FastAPI
from fastapi_pagination.ext import databases
from sqlalchemy import create_engine
from httpx import AsyncClient

from src.app.core.config import get_settings


@pytest.fixture
def set_env_type():
    os.environ['ENVIRONMENT_TYPE'] = "test"


@pytest.fixture(name="app")
def app() -> FastAPI:
    from src.main import get_application

    return get_application()


@pytest.fixture(name="client")
def client_fixture(database: Database, app: FastAPI):
    from src.app.db.database import get_database

    def get_db_override():
        return database

    app.dependency_overrides[get_database] = get_db_override
    client = AsyncClient(app=app, base_url='http://localhost:8000')
    yield client
    app.dependency_overrides.clear()


@pytest.fixture(name="database")
def database_fixture(set_env_type):
    settings = get_settings()
    from src.app.db.base import Base
    engine = create_engine(
        settings.get_db_url()
    )
    Base.metadata.create_all(bind=engine)
    database = databases.Database(settings.get_db_url())
    yield database
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(name="register")
async def test_register(client: AsyncClient):
    data = {
        "email": "user@example.com",
        "username": "string",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "password_confirm": "string"
    }

    async with client as c:
        response = await c.post("auth/register", json=data)
    assert response.status_code == 201


@pytest.fixture(name="login")
async def login(client: AsyncClient, register):
    data = {
        'username': 'user@example.com',
        'password': 'string',
    }

    async with client as c:
        response = await c.post("auth/jwt/login", data=data)
    return response
