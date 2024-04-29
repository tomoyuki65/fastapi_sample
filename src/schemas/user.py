from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

# モデル定義
class User(BaseModel):
    id: Optional[int] = Field(None, example=1)
    uid: Optional[str] = Field(None, example="XX12YY45CC123")
    name: Optional[str] = Field(None, example="田中 太郎")
    email: Optional[str] = Field(None, example="taro123@example.com")
    created_at: Optional[datetime] = Field(None, example="2024-04-29 16:33:20")
    updated_at: Optional[datetime] = Field(None, example="2024-04-29 16:33:20")
    deleted_at: Optional[datetime] = Field(None, example="2024-04-29 16:33:20")

    model_config = ConfigDict(
        # DBから取得したデータをオブジェクトに変換
        from_attributes=True,
        # 日付項目のフォーマット変換
        json_encoders = {
            datetime: lambda dt: dt.strftime("%Y-%m-%d %H:%M:%S")
        }
    )

# リクエスト定義
class UserCreate(BaseModel):
    uid: str = Field(example="XX12YY45CC123")
    name: str = Field(example="田中 太郎")
    email: str = Field(example="taro123@example.com")

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, example="田中 太郎")
    email: Optional[str] = Field(None, example="taro123@example.com")

# レスポンス定義
class UserNotFound(BaseModel):
    detail: str = Field(example="User not found")