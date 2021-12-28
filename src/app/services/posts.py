import uuid

from fastapi import HTTPException
from pydantic import UUID4
from starlette import status

from src.app.db.base import database
from ..schemas.posts import PostCreate, PostUpdate, Post
from ..models.post import posts


async def get_post(user_id: UUID4, post_id: UUID4):
    query = posts.select().where(posts.c.id == post_id and posts.c.user_id == user_id)
    return await database.fetch_one(query=query)


async def get_posts():
    db_posts = await database.fetch_all(query=posts.select())
    return db_posts


async def create_posts(user_id: UUID4, post_data: PostCreate):
    post = Post(id=uuid.uuid4(), user_id=user_id, **post_data.dict())
    query = posts.insert().values(**post_data.dict(), user_id=user_id, id=post.id)
    await database.execute(query)
    return post.dict()


async def update_post(user_id: UUID4, post_id: UUID4, post_data: PostUpdate):
    db_post = await get_post(user_id=user_id, post_id=post_id)
    if not db_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'post_id': str(post_id), **post_data.dict()}
        )
    post = Post.from_orm(db_post)
    for key, value in post_data.dict(exclude_unset=True).items():
        setattr(post, key, value)
    query = posts.update().where(posts.c.user_id == user_id, posts.c.id == post_id).values(**post.dict())
    await database.execute(query=query)
    return post


async def delete_post(user_id: UUID4, post_id: UUID4):
    query = posts.delete().where(posts.c.user_id == user_id, posts.c.id == post_id)
    await database.execute(query=query)
    return None

