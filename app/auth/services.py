from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.auth.models import User


async def get_all_users(db: AsyncSession):
    result = await db.execute(select(User))
    users = result.scalars().all()[:1000]
    return users
