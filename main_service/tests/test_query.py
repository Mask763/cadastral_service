import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_query_without_auth(async_client: AsyncClient):
    query_data = {
        "cadastral_number": "123",
        "latitude": 55.7558,
        "longitude": 37.6173,
    }
    response = await async_client.post("/query", json=query_data)
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_create_query(async_client: AsyncClient, auth_headers: dict):
    query_data = {
        "cadastral_number": "123",
        "latitude": 55.7558,
        "longitude": 37.6173,
    }
    response = await async_client.post(
        "/query",
        json=query_data,
        headers=auth_headers,
    )
    assert response.status_code == 200
    assert response.json()["cadastral_number"] == "123"
