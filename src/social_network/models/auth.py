from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from pydantic.json import isoformat
from datetime import date


class BaseUser(BaseModel):
    email: str
    username: str


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: int
    date_register: date
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True
        json_encoders = {
            date: isoformat
        }


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
