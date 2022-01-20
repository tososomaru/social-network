import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

from src.app.db.base import Base


class ModelProfile(Base):
    __tablename__ = 'user_profile'
    user_id = sa.Column(UUID, sa.ForeignKey('user.id'), primary_key=True)
    first_name = sa.Column(sa.String, nullable=True)
    last_name = sa.Column(sa.String, nullable=True)
    short_name = sa.Column(sa.String, nullable=True)
    sex = sa.Column(sa.Integer, nullable=True)

