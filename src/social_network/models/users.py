import datetime

from pydantic import BaseModel
from datetime import date


class UserBase(BaseModel):
    username: str
    password: str


class User(UserBase):
    id: int
    date_register: date

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass
