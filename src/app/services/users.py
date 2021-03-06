from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from app.app.core.settings import settings
from app.app.models.users import get_user_db
from app.app.schemas.user import UserCreate, UserDB, User, UserUpdate


class UserManager(BaseUserManager[UserCreate, UserDB]):
    user_db_model = UserDB
    reset_password_token_secret = settings.JWT_SECRET
    verification_token_secret = settings.JWT_SECRET

    async def on_after_register(self, user: UserDB, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(self, user: UserDB, token: str, request: Optional[Request] = None):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(self, user: UserDB, token: str, request: Optional[Request] = None):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


jwt_authentication = JWTAuthentication(
    secret=settings.JWT_SECRET, lifetime_seconds=3600, tokenUrl="auth/jwt/login"
)

fastapi_users = FastAPIUsers(
    get_user_manager,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

current_active_user = fastapi_users.current_user(active=True)
