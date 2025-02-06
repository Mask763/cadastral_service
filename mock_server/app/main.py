from fastapi import FastAPI
import asyncio
import random


app = FastAPI()


@app.get("/result")
async def get_result():
    # Эмуляция задержки обработки запроса
    delay = random.randint(1, 60)
    await asyncio.sleep(delay)
    
    # Случайный ответ
    response = random.choice([True, False])
    return {"result": response}
