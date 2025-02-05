import asyncio
import random


async def mock_external_server():
    await asyncio.sleep(random.randint(1, 60))
    return random.choice([True, False])
