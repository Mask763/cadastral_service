from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import current_active_user
from app.crud import create_query, get_all_queries, get_queries_by_number
from app.db import get_session
from app.schemas import (
    QueriesResponseSchema, QueryCreateSchema, QueryResponseSchema
)
from app.models import User
from app.utils import fetch_external_server_result


api_router = APIRouter()


@api_router.get("/ping")
async def ping():
    return {"status": "Server is working"}


@api_router.post("/query", response_model=QueryResponseSchema)
async def create_new_query(
    query: QueryCreateSchema,
    session: AsyncSession = Depends(get_session),
    user: User = Depends(current_active_user)
):
    responce = await fetch_external_server_result()

    if responce not in [True, False]:
        raise Exception("Unexpected responce of external server")

    db_query = await create_query(session, query, responce)
    return db_query


@api_router.get("/history", response_model=list[QueriesResponseSchema])
async def read_history(
    session: AsyncSession = Depends(get_session),
    user: User = Depends(current_active_user),
    skip: int = 0,
    limit: int = 10
):
    queries = await get_all_queries(session, skip, limit)
    return queries


@api_router.get(
    "/history/{number}", response_model=list[QueriesResponseSchema]
)
async def read_history_by_number(
    number: str,
    session: AsyncSession = Depends(get_session),
    user: User = Depends(current_active_user)
):
    queries = await get_queries_by_number(session, number)
    return queries


@api_router.get("/result")
async def get_response(user: User = Depends(current_active_user)):
    response = await fetch_external_server_result()
    return {"result": response}
