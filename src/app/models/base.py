import uuid

import sqlalchemy as sa
from fastapi_users_db_sqlalchemy import GUID


class BaseModelDB:
    id: uuid.UUID = sa.Column(GUID, primary_key=True)
