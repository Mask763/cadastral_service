from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import create_query, get_all_queries, get_queries_by_number
from app.db import get_session
from app.utils import mock_external_server
from app.schemas import QueryCreateSchema, QueryResponseSchema


api_router = APIRouter()


@api_router.get("/ping")
async def ping():
    return {"status": "Server is working"}


@api_router.post("/query", response_model=QueryResponseSchema)
async def create_new_query(
    query: QueryCreateSchema, session: AsyncSession = Depends(get_session)
):
    responce = await mock_external_server()

    if responce not in [True, False]:
        raise Exception("Unexpected responce of external server")

    db_query = await create_query(session, query, responce)
    return db_query


@api_router.get("/history", response_model=list[QueryResponseSchema])
async def read_history(
    session: AsyncSession = Depends(get_session),
    skip: int = 0,
    limit: int = 10
):
    queries = await get_all_queries(session, skip, limit)
    return queries


@api_router.get("/history/{number}", response_model=list[QueryResponseSchema])
async def read_history_by_number(
    number: str, session: AsyncSession = Depends(get_session)
):
    queries = await get_queries_by_number(session, number)
    return queries


@api_router.get("/result")
async def get_response():
    response = await mock_external_server()
    return {"result": response}
