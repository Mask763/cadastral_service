from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Query
from app.schemas import QueryCreateSchema


async def creare_query(
    session: AsyncSession, query: QueryCreateSchema, response: bool
):
    new_query = Query(**query.model_dump(), response=response)
    session.add(new_query)
    return new_query


async def get_queries_by_number(session: AsyncSession, number: str):
    query = select(Query).where(Query.cadastral_number == number)
    result = await session.execute(query)
    return result.scalars().all()


async def get_all_queries(
    session: AsyncSession, skip: int = 0, limit: int = 10
):
    query = select(Query).offset(skip).limit(limit)
    result = await session.execute(query)
    return result.scalars().all()
