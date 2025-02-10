from fastapi import FastAPI

from app.api import api_router
from app.auth import auth_backend, fastapi_users
from app.schemas import UserCreate, UserRead


app = FastAPI()

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"]
)
app.include_router(api_router, tags=["main_api"])
