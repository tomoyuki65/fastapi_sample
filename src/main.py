from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
# ルーターのインポート
from routers import sample
from routers import user
# コンフィグのインポート
import config
from database import get_db

app = FastAPI()

# ルーティング追加
app.include_router(sample.router)
app.include_router(user.router)

@app.get("/")
def root():
    return PlainTextResponse("Hello World !!")

# 環境変数の確認
@app.get("/env")
def env():
    data = {
        "ENV": config.settings.env,
        "TZ": config.settings.tz,
        "MYSQL_DATABASE": config.settings.mysql_database,
        "MYSQL_USER": config.settings.mysql_user,
        "MYSQL_PASSWORD": config.settings.mysql_password,
        "MYSQL_ROOT_PASSWORD": config.settings.mysql_root_password,
    }
    return data