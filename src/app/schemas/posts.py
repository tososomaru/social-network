import uuid
from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class Reaction(str, Enum):
    NO_REACTION = 'NO_REACTION'
    LIKE = 'LIKE'
    DISLIKE = 'DISLIKE'


class PostBase(BaseModel):
    text: str = Field(
        ...,
        metadata=dict(title='Текст поста')
    )

    class Config:
        schema_extra = {
            'example': {
                'text': 'It a example text',
            }
        }


class Post(PostBase):
    id: UUID = Field(default_factory=uuid.uuid4)
    user_id: UUID
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    viewed: bool = Field(False)
    reaction: Reaction = Field(Reaction.NO_REACTION)
    count_views: int = Field(0)
    count_likes: int = Field(0)
    count_dislikes: int = Field(0)

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                **PostBase.Config.schema_extra.get('example'),
                'id': '0',
                'user_id': 'UUID4 user'
            }
        }


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    text: str = Field(None, metadata=dict(title='Текст поста'))
    viewed: Optional[bool]
    reaction: Optional[Reaction]
