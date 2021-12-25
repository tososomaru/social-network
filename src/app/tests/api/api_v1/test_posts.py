import pytest
from starlette.testclient import TestClient

from src.app.core.settings import settings
from ..utils import login, register, get_superuser_token_headers


class TestPostsEndpoint:

    @pytest.mark.usefixtures("test_db_session")
    def test_get_posts(self, client: TestClient):
        r = client.get(f"{settings.API_V1_STR}/posts/")
        assert r.status_code == 200

    @pytest.mark.usefixtures("test_db_session")
    def test_crud_post(self, client: TestClient):
        register(client)
        headers = get_superuser_token_headers(client)
        r = client.post(
            f"{settings.API_V1_STR}/posts/",
            headers=headers,
            json={'text': 'test_post'}
        )
        r = client.get(
            f"{settings.API_V1_STR}/posts/{r.json()['id']}",
            headers=headers
        )

        r = client.put(
            f"{settings.API_V1_STR}/posts/{r.json()['id']}",
            headers=headers,
            json={'text': 'change_post'}
        )

        client.delete(
            f"{settings.API_V1_STR}/posts/{r.json()['id']}",
            headers=headers
        )

        assert r.status_code == 200

