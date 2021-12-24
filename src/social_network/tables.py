import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

import datetime


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.CHAR(100))
    password = sa.Column(sa.CHAR(50))
    date_register = sa.Column(sa.DATE, default=datetime.date.today())
