import pytest
from httpx import AsyncClient, Timeout
import pytest_asyncio

from app.main import app


@pytest_asyncio.fixture
async def async_client():
    async with AsyncClient(
        base_url="http://localhost:8000",
        timeout=Timeout(61.0)
    ) as client:
        yield client

@pytest_asyncio.fixture
async def auth_headers(async_client: AsyncClient):
    # Регистрация пользователя
    register_data = {
        "email": "test@example.com",
        "password": "testpassword",
    }
    await async_client.post("/auth/register", json=register_data)

    # Авторизация пользователя
    login_data = {
        "username": "test@example.com",
        "password": "testpassword",
    }
    response = await async_client.post("/auth/jwt/login", data=login_data)
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
