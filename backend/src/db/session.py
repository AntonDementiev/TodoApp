from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from src.settings import DATABASE_URL

engine = create_async_engine(DATABASE_URL, future=True, echo=True)

async_session =  sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_db(): 
    try:
        session: AsyncSession = async_session()
        yield session
    finally: 
        await session.close()