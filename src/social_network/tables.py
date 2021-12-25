import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

import datetime


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.Text(100), unique=True)
    username = sa.Column(sa.Text(100), unique=True)
    password_hash = sa.Column(sa.Text)
    date_register = sa.Column(sa.Date, default=datetime.date.today())
    is_superuser = sa.Column(sa.Boolean, default=False)
    is_active = sa.Column(sa.Boolean, default=False)


class Post(Base):
    __tablename__ = 'posts'

    id = sa.Column(sa.Integer, primary_key=True)
    text = sa.Column(sa.Text)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
