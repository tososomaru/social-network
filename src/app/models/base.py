import sqlalchemy as sa
from sqlalchemy_utils import UUIDType


class IdModelMixin:
    id = sa.Column(UUIDType(), primary_key=True)


class TimeStampModelMixin:
    created_at = sa.Column(sa.DateTime, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
