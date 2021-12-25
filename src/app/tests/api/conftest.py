import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy_utils import database_exists, drop_database, create_database
from starlette.testclient import TestClient
from src.app.app import app
from src.app.db.base import Base
from src.app.db.session import get_session

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.sqlite3"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


def get_test_db():
    SessionLocal = sessionmaker(bind=engine)
    test_db = SessionLocal()

    try:
        yield test_db
    finally:
        test_db.close()


@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    """
    Create a clean database on every test case.
    We use the `sqlalchemy_utils` package here for a few helpers in consistently
    creating and dropping the database.
    """
    if database_exists(SQLALCHEMY_DATABASE_URL):
        drop_database(SQLALCHEMY_DATABASE_URL)
    create_database(SQLALCHEMY_DATABASE_URL)  # Create the test database.
    Base.metadata.create_all(engine)  # Create the tables.
    app.dependency_overrides[get_session] = get_test_db  # Mock the Database Dependency
    yield  # Run the tests.
    drop_database(SQLALCHEMY_DATABASE_URL)  # Drop the test database.


@pytest.fixture
def test_db_session():
    """Returns an sqlalchemy session, and after the test tears down everything properly."""

    SessionLocal = sessionmaker(bind=engine)

    session: Session = SessionLocal()
    yield session
    # Drop all data after each test
    for tbl in reversed(Base.metadata.sorted_tables):
        engine.execute(tbl.delete())
    # put back the connection to the connection pool
    session.close()


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c