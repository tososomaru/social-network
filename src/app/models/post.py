import sqlalchemy as sa
from sqlmodel.sql.sqltypes import GUID

from src.app.db.base import Base
from src.app.models.user import users
from src.app.models.base import IdModelMixin, TimeStampModelMixin


class Post(Base, IdModelMixin, TimeStampModelMixin):
    __tablename__ = 'post'

    text = sa.Column(sa.Text, nullable=True)
    user_id = sa.Column(GUID, sa.ForeignKey(users.c.id), nullable=False)
    viewed = sa.Column(sa.Boolean, default=sa.sql.expression.false())
    reaction = sa.Column(sa.String(30), server_default=sa.text('NO_REACTION'))
    count_views = sa.Column(sa.Integer, default=sa.text('0'))
    count_likes = sa.Column(sa.Integer(), default=sa.text('0'))
    count_dislikes = sa.Column(sa.Integer(), default=sa.text('0'))


posts: sa.Table = Post.__table__
