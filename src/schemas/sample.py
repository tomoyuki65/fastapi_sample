from pydantic import BaseModel, Field

class SampleStr(BaseModel):
    message: str = Field(example="メッセージ")
