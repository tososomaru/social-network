import uuid

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


class BaseModelDB:
    id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
