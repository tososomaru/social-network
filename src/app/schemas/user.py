from typing import Optional

from pydantic import validator
from datetime import datetime
from fastapi_users import models

from src.app.schemas.base import TimeStampSchemaMixin, IdSchemaMixin
from src.app.schemas.utils import convert_datetime_to_iso_8601


class User(models.BaseUser, IdSchemaMixin, TimeStampSchemaMixin):
    username: str

    # TODO: добавить проверку на существующий логин в бд

    class Config:
        json_encoders = {
            datetime: convert_datetime_to_iso_8601
        }


class UserCreate(models.BaseUserCreate):
    username: str
    password_confirm: str

    @validator("password_confirm")
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values["password"]:
            raise ValueError({
                'error': True,
                'type': 'ValidationError',
                'field': 'password_confirm',
                'error_status': 200,
                'text': 'Passwords don`t match',
                'body': v}
            )
        return v


class UserUpdate(models.BaseUserUpdate):
    username: Optional[str]


class UserDB(User, models.BaseUserDB):
    username: str
