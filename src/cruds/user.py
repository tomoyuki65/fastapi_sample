from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from sqlalchemy.engine import Result
from typing import List, Optional, Tuple
import models.user as user_model
import schemas.user as user_schema
from datetime import datetime

# ユーザー作成
async def create_user(
    db: AsyncSession,
    user_create: user_schema.UserCreate
) -> user_model.User:
    user = user_model.User(**user_create.model_dump())
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

# ユーザーを１件取得
async def get_user(
    db: AsyncSession,
    user_uid: str
) -> Optional[user_model.User]:
    result: Result = await db.execute(
        select(
            user_model.User.id,
            user_model.User.uid,
            user_model.User.name,
            user_model.User.email,
            user_model.User.created_at,
            user_model.User.updated_at,
            user_model.User.deleted_at
        ).filter(
            user_model.User.uid == user_uid
        )
    )
    return result.first()

# ユーザー更新
async def update_user(
    db: AsyncSession,
    user_update: user_schema.UserUpdate,
    user_uid: str,
    original: user_model.User
):
    update_name: str
    if user_update.name:
        update_name = user_update.name
    else:
        update_name = original.name
    
    update_email: str
    if user_update.email:
        update_email = user_update.email
    else:
        update_email = original.email

    # 更新処理
    result = await db.execute(
        update(user_model.User)
        .values(
            name=update_name,
            email=update_email,
            updated_at=datetime.now()
        )
        .where(user_model.User.uid == user_uid)
    )
    await db.commit()

# ユーザーを論理削除
async def delete_user(
    db: AsyncSession,
    user_uid: str,
    original: user_model.User
):
    # 更新処理
    result = await db.execute(
        update(user_model.User)
        .values(
            updated_at=datetime.now(),
            deleted_at=datetime.now()
        )
        .where(user_model.User.uid == user_uid)
    )
    await db.commit()

# ユーザーを全件取得（削除済み含む）
async def get_users(
    db: AsyncSession
) -> List[user_model.User]:
    result: Result = await db.execute(
        select(
            user_model.User.id,
            user_model.User.uid,
            user_model.User.name,
            user_model.User.email,
            user_model.User.created_at,
            user_model.User.updated_at,
            user_model.User.deleted_at
        ).execution_options(include_deleted=True)
    )
    return result.all()