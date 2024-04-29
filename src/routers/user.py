from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from typing import List, Optional
import models.user as user_model
import schemas.user as user_schema
import schemas.common as common_schema
import cruds.user as user_crud

router = APIRouter()

# ユーザー作成
@router.post("/user",
    status_code=201,
    responses={
        201: { "model": common_schema.OK },
    },
)
async def create_user(
    user_body: user_schema.UserCreate,
    db: AsyncSession = Depends(get_db)
):
    await user_crud.create_user(db, user_body)
    return { "message": "OK" }

# ユーザーを１件取得
@router.get("/user/{user_uid}",
    response_model=Optional[user_schema.User]
)
async def a_user(
    user_uid: str,
    db: AsyncSession = Depends(get_db)
):
    return await user_crud.get_user(db, user_uid)

# ユーザー更新
@router.put("/user/{user_uid}",
    status_code=200,
    responses={
        200: { "model": common_schema.OK },
        404: { "model": user_schema.UserNotFound },
    },
)
async def update_user(
    user_uid: str,
    user_body: user_schema.UserUpdate,
    db: AsyncSession = Depends(get_db)
):
    user = await user_crud.get_user(db, user_uid)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    await user_crud.update_user(db, user_body, user_uid, user)
    return { "message": "OK" }

# ユーザー削除
@router.delete("/user/{user_uid}",
    status_code=200,
    responses={
        200: { "model": common_schema.OK },
        404: { "model": user_schema.UserNotFound },
    },
)
async def delete_user(
    user_uid: str,
    db: AsyncSession = Depends(get_db)
):
    user = await user_crud.get_user(db, user_uid)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    await user_crud.delete_user(db, user_uid, user)
    return { "message": "OK" }

# ユーザーを全件取得
@router.get("/users",
    response_model=Optional[List[user_schema.User]]
)
async def list_users(db: AsyncSession = Depends(get_db)):
    return await user_crud.get_users(db)