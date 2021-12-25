from datetime import datetime

import sqlalchemy as sa

from src.app.db.base import Base


class ModelUser(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    email = sa.Column(sa.Text(100), unique=True, index=True, nullable=False)
    username = sa.Column(sa.Text(100), unique=True, index=True, nullable=False)
    hashed_password = sa.Column(sa.String, nullable=False)
    created_at = sa.Column(sa.DateTime, default=datetime.utcnow)
    updated_at = sa.Column(sa.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_superuser = sa.Column(sa.Boolean(), default=False)
    is_active = sa.Column(sa.Boolean(), default=False)