from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
# ルーターのインポート
from routers import sample

app = FastAPI()

# ルーティング追加
app.include_router(sample.router)

@app.get("/")
def root():
    return PlainTextResponse("Hello World !!")
