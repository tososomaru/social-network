from fastapi import APIRouter
from fastapi import Depends, Response, status

from typing import List

from ..models.users import User, UserCreate, UserUpdate
from ..services.users import UserService

router = APIRouter(
    prefix='/users'
)


@router.get('/', response_model=List[User])
def get_users(service: UserService = Depends()):
    return service.get_users()


@router.get('/{user_id}', response_model=User)
def get_user(
        user_id: int,
        service: UserService = Depends()
):
    return service.get_user_by_id(user_id)


@router.post('/register/', response_model=User)
def create_user(
        user_data: UserCreate,
        service: UserService = Depends()
):
    return service.create_user(user_data)


@router.put('/{user_id}', response_model=User)
def get_user(
        user_id: int,
        user_data: UserUpdate,
        service: UserService = Depends()
):
    return service.update_user(user_id, user_data)


@router.delete('/{user_id}', response_model=User)
def delete_user(
        user_id: int,
        service: UserService = Depends()
):
    service.delete_user(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)




