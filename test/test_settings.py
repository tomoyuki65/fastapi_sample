import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.database import Base
from src.main import app
import starlette.status
from alembic.config import Config
from alembic import command

# 各ルーターのget_dbインスタンスをインポート
from src.routers.user import get_db

ASYNC_DB_URL = "{}://{}:{}@{}:{}/{}?charset={}".format(
    "mysql+aiomysql",
    "test_fastapi_sample_user",
    "test_fastapi_sample_password",
    "test-db",
    "3307",
    "test_fastapi_sample_db",
    "utf8mb4"
)

@pytest_asyncio.fixture()
async def async_client() -> AsyncClient:
    # テスト用DBへのテーブル作成
    alembic_cfg = Config("alembic_test.ini")
    command.upgrade(alembic_cfg, "head")

    # DB設定をテスト用DBにオーバーライド
    async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
    async_session = sessionmaker(
                        autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
                    )
    async def get_test_db():
        async with async_session() as session:
            yield session
    app.dependency_overrides[get_db] = get_test_db

    # テスト用に非同期HTTPクライアントを返却
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client
    
    # セッションクローズ
    await async_engine.dispose()

    # テスト用DBのテーブル削除
    command.downgrade(alembic_cfg, "base")