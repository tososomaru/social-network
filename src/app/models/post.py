from datetime import datetime
import uuid
# from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import SQLModel, Field

from src.app.db.base import Base
from src.app.models.base import BaseModelDB


class Post(Base, BaseModelDB):
    __tablename__ = 'post'

    text = sa.Column(sa.Text, nullable=True)
    user_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey("user.id"), nullable=False)
    created_at = sa.Column(sa.DateTime, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    viewed = sa.Column(sa.Boolean, default=sa.sql.expression.false())
    reaction = sa.Column(sa.String(30), default=sa.text('NO_REACTION'))
    count_views = sa.Column(sa.Integer, default=sa.text('0'))
    count_likes = sa.Column(sa.Integer(), default=sa.text('0'))
    count_dislikes = sa.Column(sa.Integer(), default=sa.text('0'))


posts: sa.Table = Post.__table__

# class PostBase(SQLModel):
#     text: str
#     user_id: UUID
#     created_at: datetime = Field(default_factory=datetime.now, )
#
#
# class Post(PostBase, table=True):
#     id = Field(default_factory = uuid.uuid4, primary_key = True)

