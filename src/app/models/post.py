import sqlalchemy as sa

from src.app.db.base import Base


class Post(Base):
    __tablename__ = 'posts'

    id = sa.Column(sa.Integer, primary_key=True)
    text = sa.Column(sa.Text)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))