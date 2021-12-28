import uuid

import pytest
from databases import Database
from httpx import AsyncClient, Response

from src.app.models.post import posts
from src.app.schemas.posts import Post


@pytest.fixture(name="register")
async def register(client: AsyncClient):
    data = {
        "email": "user@example.com",
        "password": "string",
        "is_active": True,
        "is_superuser": True,
        "is_verified": True,
        "username": "string",
        "password_confirm": "string"
    }

    async with client as c:
        response = await c.post("auth/login", data=data)

    assert response.status_code == 201


@pytest.fixture(name="login")
async def login(client: AsyncClient):
    data = {
        "username": "user@example.com",
        "password": "string",
    }
    async with client as c:
        response = await c.post("auth/jwt/login", data=data)

    return response


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
async def test_get_posts(client: AsyncClient):
    async with client as c:
        response = await c.get("api/v1/posts")

    assert response.status_code == 200
    assert len(response.json()['items']) > 0


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


