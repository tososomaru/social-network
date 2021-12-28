from datetime import datetime

import sqlalchemy as sa
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from src.app.db.base import Base, database
from src.app.schemas.user import UserDB


class ModelUser(Base, SQLAlchemyBaseUserTable):
    username = sa.Column(sa.Text(100), unique=True, index=True, nullable=False)
    created_at = sa.Column(sa.DateTime, default=datetime.utcnow)
    updated_at = sa.Column(sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


users = ModelUser.__table__


async def get_user_db():
    yield SQLAlchemyUserDatabase(UserDB, database, users)


class ModelProfile(Base):
    __tablename__ = 'user_profile'
    pass