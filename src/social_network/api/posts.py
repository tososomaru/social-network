from fastapi import APIRouter
from fastapi import Depends, Response, status

from typing import List

from ..models.auth import User
from ..models.posts import Post, PostCreate, PostUpdate
from ..services.auth import get_current_user
from ..services.posts import PostService

router = APIRouter(
    prefix='/posts',
    tags=['posts']
)


@router.get('/', response_model=List[Post])
def get_posts(
        user: User = Depends(get_current_user),
        service: PostService = Depends()
):
    return service.get_posts(user_id=user.id)


@router.get('/{post_id}', response_model=Post)
def get_post(
        post_id: int,
        user: User = Depends(get_current_user),
        service: PostService = Depends()
):
    return service.get_post_by_id(user_id=user.id, post_id=post_id)


@router.post('/', response_model=Post)
def create_post(
        post_data: PostCreate,
        user: User = Depends(get_current_user),
        service: PostService = Depends()
):
    return service.create_post(user_id=user.id, post_data=post_data)


@router.put('/{post_id}', response_model=Post)
def update_post(
        post_id: int,
        post_data: PostUpdate,
        user: User = Depends(get_current_user),
        service: PostService = Depends()
):
    return service.update_post(user_id=user.id, post_id=post_id, post_data=post_data)


@router.delete('/{post_id}', response_model=Post)
def delete_post(
        post_id: int,
        user: User = Depends(get_current_user),
        service: PostService = Depends()
):
    service.delete_post(user_id=user.id, post_id=post_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)




