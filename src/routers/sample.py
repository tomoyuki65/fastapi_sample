from fastapi import APIRouter, HTTPException
# スキーマのインポート
import schemas.sample as sample_schema
import schemas.common as common_schema

router = APIRouter()

@router.get("/sample",
    # デフォルトのレスポンスステータスコード
    status_code=200,
    # レスポンススキーマの種類
    responses={
        200: { "model": sample_schema.SampleStr },
    },
)
async def sample_str():
    return sample_schema.SampleStr(message="サンプル")

# 例外処理あり
@router.get("/sample-exception",
    # デフォルトのレスポンスステータスコード
    status_code=201,
    # レスポンススキーマの種類
    responses={
        201: { "model": sample_schema.SampleStr },
        500: { "model": common_schema.InternalServerError },
    },
)
async def sample_str():
    try:
        return sample_schema.SampleStr(message="サンプル")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))