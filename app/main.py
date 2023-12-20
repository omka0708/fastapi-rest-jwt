from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.auth import auth_backend, fastapi_users, current_user
from app.auth.models import User
from app.auth.schemas import UserRead, UserCreate
from app.auth import services
from app.database import get_async_session

app = FastAPI()

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/api/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/api/auth",
    tags=["auth"],
)


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url='/docs')


@app.get("/api/users", tags=["auth"])
async def get_all_users(session: AsyncSession = Depends(get_async_session)):
    return await services.get_all_users(session)


@app.get("/api/current_user", tags=["auth"])
async def get_current_user(user: User = Depends(current_user)):
    return f"Hello, {user.email}"
