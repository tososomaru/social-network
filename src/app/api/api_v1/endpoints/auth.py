from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.app.schemas.auth import UserCreate, Token, User
from src.app.services.auth import AuthService, get_current_user

router = APIRouter()


@router.post('/register/', response_model=Token)
def sign_up(
        user_data: UserCreate,
        service: AuthService = Depends()
):
    return service.register_new_user(user_data)


@router.post('/login/', response_model=Token)
def sign_in(
        form_data: OAuth2PasswordRequestForm = Depends(),
        service: AuthService = Depends()
):
    return service.authenticate_user(form_data.username, form_data.password)


@router.get('/me/', response_model=User)
def get_user(user: User = Depends(get_current_user)):
    return user
