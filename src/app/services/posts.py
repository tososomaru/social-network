from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.app.db.session import get_session
from ..schemas.posts import PostCreate, PostUpdate
from ..models.post import Post


class PostService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int, post_id: int) -> Post:
        post = (
            self.session
            .query(Post)
            .filter(
                Post.id == post_id,
                Post.user_id == user_id
            )
            .first()
        )
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return post

    def get_posts(self) -> List[Post]:
        return (
            self.session
            .query(Post)
            .order_by(Post.id.asc())
            .all()
        )

    def get_post_by_id(self, user_id: int, post_id: int) -> Post:
        return self._get(user_id, post_id)

    def create_post(self, user_id: int, post_data: PostCreate) -> Post:
        post = Post(**post_data.dict(), user_id=user_id)
        self.session.add(post)
        self.session.commit()
        return post

    def update_post(self, user_id: int, post_id: int, post_data: PostUpdate) -> Post:
        post = self.get_post_by_id(user_id, post_id)
        for k, v in post_data:
            setattr(post, k, v)
        self.session.commit()
        return post

    def delete_post(self,user_id: int, post_id: int) -> None:
        post = self._get(user_id, post_id)
        self.session.delete(post)
        self.session.commit()
