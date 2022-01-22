import sqlalchemy as sa
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from src.app.db.base import Base


class ModelUser(Base, SQLAlchemyBaseUserTable):
    # id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = sa.Column(sa.String(100), unique=True, index=True, nullable=False)
    created_at = sa.Column(sa.DateTime, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, server_default=sa.func.now(), server_onupdate=sa.func.now())


users = ModelUser.__table__