from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import config

DATABASE_URL = "{}://{}:{}@{}:{}/{}?charset={}".format(
    "mysql+aiomysql",
    config.settings.mysql_user,
    config.settings.mysql_password,
    "db",
    "3306",
    config.settings.mysql_database,
    "utf8mb4"
)

async_engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

Base = declarative_base()

async def get_db():
    async with async_session() as session:
        yield session