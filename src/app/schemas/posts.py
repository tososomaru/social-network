import uuid
from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from app.app.schemas.utils import convert_datetime_to_iso_8601


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
        json_encoders = {
            datetime: convert_datetime_to_iso_8601
        }

        schema_extra = {
            'example': {
                'text': 'It a example text',
            }
        }


class Post(PostBase):
    id: UUID = Field(default_factory=uuid.uuid4, metadata=dict(title='id'))
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
                'id': uuid.uuid4(),
                'user_id': uuid.uuid4(),
                'created_at': datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
                'updated_at': datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
                'viewed': False,
                'reaction': Reaction.NO_REACTION,
                'count_views': 0,
                'count_likes': 0,
                'count_dislikes': 0
            }
        }


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    text: str = Field(None, metadata=dict(title='Текст поста'))
    viewed: Optional[bool]
    reaction: Optional[Reaction]

    class Config:
        schema_extra = {
            'example': {
                **PostBase.Config.schema_extra.get('example'),
                'viewed': False,
                'reaction': Reaction.NO_REACTION,
            }
        }
