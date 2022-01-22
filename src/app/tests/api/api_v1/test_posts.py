import uuid

import pytest
from databases import Database
from httpx import AsyncClient, Response

from src.app.models.post import posts
from src.app.schemas.posts import Post


def create_headers_with_token_from_content(response: Response):
    return {
        'Authorization': f"Bearer {response.json()['access_token']}"
    }


@pytest.mark.asyncio
async def test_create_post(client: AsyncClient, login):
    headers = create_headers_with_token_from_content(login)
    data = {
        "text": "It a example text"
    }
    async with client as c:
        response = await c.post("api/v1/posts", headers=headers, json=data)
    assert response.status_code == 201
    assert response.json()['text'] == "It a example text"


@pytest.mark.asyncio
async def test_get_posts(database: Database, client: AsyncClient):
    data = {
        "text": "It a example text2"
    }
    post = Post(id=uuid.uuid4(), user_id=uuid.uuid4(), **data)
    query = posts.insert().values(**data, user_id=post.user_id, id=post.id)
    await database.execute(query)
    async with client as c:
        response = await c.get("api/v1/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.asyncio
async def test_get_post_by_id(database: Database, client: AsyncClient, login):
    headers = create_headers_with_token_from_content(login)
    data = {
        "text": "It a example text"
    }
    post = Post(id=uuid.uuid4(), user_id=uuid.uuid4(), **data)
    query = posts.insert().values(**data, user_id=post.user_id, id=post.id)
    await database.execute(query)

    async with client as c:
        response = await c.get(f"api/v1/posts/{post.id}", headers=headers)

    content = response.json()
    assert response.status_code == 200
    assert content['id'] == str(post.id)


@pytest.mark.asyncio
async def test_delete_post(database: Database, client: AsyncClient, login):
    headers = create_headers_with_token_from_content(login)
    data = {
        "text": "It a example text"
    }
    post = Post(id=uuid.uuid4(), user_id=uuid.uuid4(), **data)
    query = posts.insert().values(**data, user_id=post.user_id, id=post.id)
    await database.execute(query)

    async with client as c:
        response = await c.delete(f"api/v1/posts/{post.id}", headers=headers)

    assert response.status_code == 204


@pytest.mark.asyncio
async def test_update_post(database: Database, client: AsyncClient, login):
    headers = create_headers_with_token_from_content(login)
    data = {
        "text": "It a example text"
    }
    post = Post(id=uuid.uuid4(), user_id=uuid.uuid4(), **data)
    query = posts.insert().values(**data, user_id=post.user_id, id=post.id)
    await database.execute(query)

    data = {
        "text": "patch"
    }

    async with client as c:
        response = await c.patch(f"api/v1/posts/{post.id}", headers=headers, json=data)

    assert response.status_code == 200
    assert response.json()['text'] == data['text']
