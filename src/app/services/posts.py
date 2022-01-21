import uuid

from databases import Database
from fastapi import HTTPException
from pydantic import UUID4
from starlette import status

from ..schemas.posts import PostCreate, PostUpdate, Post
from ..models.post import posts


async def get_post(user_id: UUID4, post_id: UUID4, db: Database) -> Post:
    query = posts.select().where(posts.c.id == post_id and posts.c.user_id == user_id)
    post_record = await db.fetch_one(query=query)
    return Post(**post_record._mapping)


async def get_posts(db: Database):
    posts_records = await db.fetch_all(query=posts.select())
    return [Post(**post._mapping) for post in posts_records]


async def create_posts(user_id: UUID4, post_data: PostCreate, db: Database):
    post = Post(id=uuid.uuid4(), user_id=user_id, **post_data.dict())
    query = posts.insert()
    await db.execute(query, post.dict())
    return post.dict()


async def update_post(user_id: UUID4, post_id: UUID4, post_data: PostUpdate, db: Database):
    db_post = await get_post(user_id=user_id, post_id=post_id, db=db)
    if not db_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'post_id': str(post_id), **post_data.dict()}
        )
    post = Post.from_orm(db_post)
    for key, value in post_data.dict(exclude_unset=True).items():
        setattr(post, key, value)
    query = posts.update().where(posts.c.user_id == user_id, posts.c.id == post_id).values(**post.dict())
    await db.execute(query=query)
    return post


async def delete_post(user_id: UUID4, post_id: UUID4, db: Database):
    query = posts.delete().where(posts.c.user_id == user_id, posts.c.id == post_id)
    await db.execute(query=query)
    return None
