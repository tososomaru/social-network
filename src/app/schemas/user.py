from typing import Optional

from pydantic import validator, EmailStr, constr
from datetime import datetime
from fastapi_users import models


def convert_datetime_to_iso_8601(dt: datetime) -> str:
    return dt.strftime('%Y-%m-%dT%H:%M:%S')


class User(models.BaseUser):
    username: str
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()

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
    pass


class UserDB(User, models.BaseUserDB):
    pass
