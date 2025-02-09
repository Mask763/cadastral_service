import httpx


async def fetch_external_server_result():
    async with httpx.AsyncClient(timeout=httpx.Timeout(61.0)) as client:
            # Отправляем запрос к эмулированному серверу
            response = await client.get("http://mock_server:8001/result")
            return response.json()["result"]
