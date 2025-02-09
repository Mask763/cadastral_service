from datetime import datetime
from pydantic import BaseModel, EmailStr

from fastapi_users import models


class UserRead(BaseModel):
    id: models.ID
    email: EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class QueryCreateSchema(BaseModel):
    cadastral_number: str
    latitude: float
    longitude: float


class QueryResponseSchema(BaseModel):
    response: bool


class QueriesResponseSchema(BaseModel):
    id: int
    cadastral_number: str
    latitude: float
    longitude: float
    response: bool
    create_at: datetime

    class Config:
        from_attributes = True
