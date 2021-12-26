from pydantic import BaseModel


class PostBase(BaseModel):
    text: str

    class Config:
        schema_extra = {
            'example': {
                'text': 'It a example text',
            }
        }


class Post(PostBase):
    id: int

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                **PostBase.Config.schema_extra.get('example'),
                'id': '0',
            }
        }


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass
