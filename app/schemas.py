from pydantic import BaseModel


class QueryCreateSchema(BaseModel):
    cadastral_number: str
    latitude: float
    longitude: float


class QueryResponseSchema(BaseModel):
    id: int
    cadastral_number: str
    latitude: float
    longitude: float
    response: bool

    class Config:
        from_attributes = True
