from sqlalchemy.orm import Session

from src.app.db.base import Base
from src.app.db.session import engine
from src.app.schemas.auth import UserCreate
from src.app.core.settings import settings
from src.app.services.users import UserService
from src.app.services.auth import AuthService


def init_db(db: Session) -> None:

    Base.metadata.create_all(bind=engine)

    user = UserService(db).get_by_email(email=settings.FIRST_SUPERUSER_EMAIL)
    if not user:
        user_data: UserCreate = UserCreate(
            email=settings.FIRST_SUPERUSER_EMAIL,
            username=settings.FIRST_SUPERUSER_LOGIN,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            password_confirm=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )

        AuthService(db).register_new_user(user_data)
