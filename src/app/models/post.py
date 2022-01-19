import sqlalchemy as sa
from fastapi_users_db_sqlalchemy import GUID

from sqlalchemy_utils import force_instant_defaults

from app.app.db.base import Base
from app.app.models.base import BaseModelDB

force_instant_defaults()


class Post(Base, BaseModelDB):
    __tablename__ = 'posts'

    text = sa.Column(sa.Text, nullable=True)
    user_id = sa.Column(GUID, sa.ForeignKey('user.id'))
    created_at = sa.Column(sa.DateTime, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, server_default=sa.func.now(), server_onupdate=sa.func.now())
    viewed = sa.Column(sa.Boolean, server_default=sa.sql.expression.false())
    reaction = sa.Column(sa.String(30), server_default=sa.text('NO_REACTION'))
    count_views = sa.Column(sa.Integer, server_default=sa.text('0'))
    count_likes = sa.Column(sa.Integer(), server_default=sa.text('0'))
    count_dislikes = sa.Column(sa.Integer(), server_default=sa.text('0'))


posts: sa.Table = Post.__table__
