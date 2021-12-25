from datetime import datetime, timedelta

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.hash import bcrypt
from jose import jwt, JWTError
from pydantic import ValidationError
from sqlalchemy.orm import Session

from src.app.db.session import get_session
from ..schemas.auth import Token, UserCreate, User as SchemeUser
from ..models.user import ModelUser
from src.app.core.settings import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login/")


def get_current_user(token: str = Depends(oauth2_scheme)) -> SchemeUser:
    return AuthService.validate_token(token)


def get_superuser(token: str = Depends(oauth2_scheme)) -> SchemeUser:
    user = AuthService.validate_token(token)
    if not user.is_superuser:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User is not superuser")
    return user


class AuthException(HTTPException):
    def __init__(self, detail):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={
                    'WWW-Authenticate': 'Bearer'
                }
        )


class AuthService:
    @classmethod
    def verify_password(
            cls,
            plain_password: str,
            hashed_password: str
    ) -> bool:
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def validate_token(cls, token: str) -> SchemeUser:

        try:
            payload = jwt.decode(
                token,
                settings.JWT_SECRET,
                algorithms=[settings.JWT_ALGORITHM]
            )

        except JWTError:
            raise AuthException('Could not validate credentials') from None

        user_data = payload.get('user')
        try:
            user = SchemeUser.parse_raw(user_data)
        except ValidationError:
            raise AuthException('User validation error') from None

        return user

    @classmethod
    def create_token(cls, user: ModelUser) -> Token:
        user_data = SchemeUser.from_orm(user)
        now = datetime.utcnow()

        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(seconds=settings.JWT_EXPIRATION),
            'sub': str(user_data.id),
            'user': user_data.json()
        }

        token = jwt.encode(
            payload,
            settings.JWT_SECRET,
            algorithm=settings.JWT_ALGORITHM
        )

        return Token(access_token=token)

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def register_new_user(self, user_data: UserCreate) -> Token:
        user = ModelUser(
            email=user_data.email,
            username=user_data.username,
            hashed_password=self.hash_password(user_data.password),
            is_superuser=user_data.is_superuser,
            is_active=True,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        self.session.add(user)
        self.session.commit()

        return self.create_token(user)

    def authenticate_user(self, username: str, password: str) -> Token:

        user = (
            self.session
            .query(ModelUser)
            .filter(ModelUser.username == username)
            .first()
        )

        if not user:
            raise AuthException('Incorrect username')

        if not self.verify_password(password, user.hashed_password):
            raise AuthException('Incorrect password')

        return self.create_token(user)






