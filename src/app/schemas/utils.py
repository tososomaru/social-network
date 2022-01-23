import logging
import uuid
from datetime import datetime


def convert_datetime_to_iso_8601(dt: datetime) -> str:
    return dt.strftime('%Y-%m-%dT%H:%M:%S')


def create_uuid_without_leading_zeros() -> uuid.UUID:
    value = uuid.uuid4()
    if value.hex[0] == '0':
        return create_uuid_without_leading_zeros()
    return value.hex
