import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register(async_client: AsyncClient):
    response = await async_client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "testpassword"},
    )
    assert response.status_code == 201
    assert "id" in response.json()

@pytest.mark.asyncio
async def test_login(async_client: AsyncClient):
    # Сначала регистрируем пользователя
    await async_client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "testpassword"},
    )

    # Пытаемся авторизоваться
    response = await async_client.post(
        "/auth/jwt/login",
        data={"username": "test@example.com", "password": "testpassword"},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
