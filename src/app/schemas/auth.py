from pydantic import BaseModel, validator, EmailStr, constr
from datetime import datetime


def convert_datetime_to_iso_8601(dt: datetime) -> str:
    return dt.strftime('%Y-%m-%dT%H:%M:%S')


class BaseUser(BaseModel):
    email: EmailStr
    username: str


class UserCreate(BaseUser):
    password: constr(min_length=8, max_length=50)
    password_confirm: str
    is_superuser: bool = False

    @validator("password_confirm")
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values["password"]:
            raise ValueError("Passwords don`t match")
        return v


class User(BaseUser):
    id: int
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    is_active: bool = False
    is_superuser: bool = False

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: convert_datetime_to_iso_8601
        }


class Token(BaseModel):
    access_token:  str
    token_type: str = 'bearer'
