
from fastapi import Depends, Response, status, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session

from src.app.schemas.user import User
from src.app.schemas.posts import Post, PostCreate, PostUpdate
from src.app.services import posts as service

from fastapi_pagination import paginate, Page, Params
from src.app.services.users import current_active_user

from fastapi import APIRouter

router = APIRouter()


@router.get('/', response_model=Page[Post])
async def get_posts(
        params: Params = Depends()
):
    return paginate(await service.get_posts(), params)


@router.get('/{post_id}', response_model=Post)
async def get_post(
        post_id: UUID4,
        user: User = Depends(current_active_user),
):
    post = await service.get_post(user_id=user.id, post_id=post_id)
    print(post)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=post_id
        )
    return post


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Post)
async def create_post(
        post_data: PostCreate,
        user: User = Depends(current_active_user),
):
    post = await service.create_posts(user_id=user.id, post_data=post_data)
    return post


@router.patch('/{post_id}', response_model=Post)
async def update_post(
        post_id: UUID4,
        post_data: PostUpdate,
        user: User = Depends(current_active_user),
):
    return await service.update_post(user_id=user.id, post_id=post_id, post_data=post_data)


@router.delete('/{post_id}')
async def delete_post(
        post_id: UUID4,
        user: User = Depends(current_active_user),
):
    post = await service.get_post(user_id=user.id, post_id=post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'post_id': post_id}
        )
    await service.delete_post(user_id=user.id, post_id=post_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
