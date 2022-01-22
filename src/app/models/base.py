import uuid

import sqlalchemy as sa
from sqlmodel.sql.sqltypes import GUID


class IdModelMixin:
    id = sa.Column(GUID, primary_key=True, default=uuid.uuid4)
