# import pytest
# from fastapi.testclient import TestClient
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# from src.app.db.init_db import init_db
# from src.app.db.session import get_session
# from src.app.db.base import Base
# from src.app.app import app
#
# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.sqlite3"
#
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     connect_args={"check_same_thread": False}
# )
# TestingSessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )
#
#
# def override_get_session():
#     session = TestingSessionLocal()
#     try:
#         yield session
#     finally:
#         session.close()
#
#
# @pytest.fixture()
# def test_db():
#     Base.metadata.create_all(bind=engine)
#     yield
#
#
# db = TestingSessionLocal()
# init_db(db)
# app.dependency_overrides[get_session] = override_get_session
#
#
# client = TestClient(app)
# Base.metadata.drop_all(bind=engine)
