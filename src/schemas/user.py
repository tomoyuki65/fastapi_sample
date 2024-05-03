from pydantic import BaseModel, ConfigDict, field_validator
from typing import Optional
from datetime import datetime

# モデル定義
class User(BaseModel):
    id: Optional[int]
    uid: Optional[str]
    name: Optional[str]
    email: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]

    # 日付のフォーマット変換 
    @field_validator("created_at")
    def parse_created_at(cls, v):
        if isinstance(v, datetime):
            return v.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(v, str):
            return datetime.strptime(v, "%Y-%m-%d %H:%M:%S")
        else:
            return None
    
    @field_validator("updated_at")
    def parse_updated_at(cls, v):
        if isinstance(v, datetime):
            return v.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(v, str):
            return datetime.strptime(v, "%Y-%m-%d %H:%M:%S")
        else:
            return None
    
    @field_validator("deleted_at")
    def parse_deleted_at(cls, v):
        if isinstance(v, datetime):
            return v.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(v, str):
            return datetime.strptime(v, "%Y-%m-%d %H:%M:%S")
        else:
            return None

    model_config = ConfigDict(
        # DBから取得したデータをオブジェクトに変換
        from_attributes=True,
        # exampleの定義
        json_schema_extra={
            "example": {
                "id": 1,
                "uid": "XX12YY45CC123",
                "name": "田中 太郎",
                "email": "taro123@example.com",
                "created_at": "2024-04-29 16:33:20",
                "updated_at": "2024-04-29 16:33:20",
                "deleted_at": "2024-04-29 16:33:20",
            }
        },
    )

# リクエスト定義
class UserCreate(BaseModel):
    uid: str
    name: str
    email: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "uid": "XX12YY45CC123",
                    "name": "田中 太郎",
                    "email": "taro123@example.com",
                }
            ]
        }
    }

class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "田中 太郎",
                    "email": "taro123@example.com",
                }
            ]
        }
    }

# レスポンス定義
class UserNotFound(BaseModel):
    detail: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "detail": "User not found",
                }
            ]
        }
    }