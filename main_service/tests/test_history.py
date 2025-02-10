import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_history(async_client: AsyncClient, auth_headers: dict):
    # Сначала создаем запрос
    query_data = {
        "cadastral_number": "123",
        "latitude": 55.7558,
        "longitude": 37.6173,
    }
    await async_client.post("/query", json=query_data, headers=auth_headers)

    # Получаем историю запросов
    response = await async_client.get("/history", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) > 0

@pytest.mark.asyncio
async def test_get_history_by_cadastral(async_client: AsyncClient, auth_headers: dict):
    # Сначала создаем запрос
    query_data = {
        "cadastral_number": "123",
        "latitude": 55.7558,
        "longitude": 37.6173,
    }
    await async_client.post("/query", json=query_data, headers=auth_headers)

    # Получаем историю по кадастровому номеру
    response = await async_client.get("/history/123", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) > 0
