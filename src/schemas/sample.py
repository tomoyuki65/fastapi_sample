from pydantic import BaseModel

class SampleStr(BaseModel):
    message: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "message": "メッセージ",
                }
            ]
        }
    }
