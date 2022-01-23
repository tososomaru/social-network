import sqlalchemy as sa
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from src.app.db.base import Base
from src.app.models.base import TimeStampModelMixin


class ModelUser(Base, SQLAlchemyBaseUserTable, TimeStampModelMixin):
    username = sa.Column(sa.String(100), unique=True, index=True, nullable=False)


users = ModelUser.__table__