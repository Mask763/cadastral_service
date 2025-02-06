import httpx
from fastapi import HTTPException


async def fetch_external_server_result():
    try:
        async with httpx.AsyncClient() as client:
            # Отправляем запрос к эмулированному серверу
            response = await client.get("http://127.0.0.1:8001/result")
            response.raise_for_status()
            return response.json()["result"]
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"External server error: {str(e)}")
