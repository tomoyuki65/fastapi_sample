from pydantic import BaseModel

class OK(BaseModel):
    message: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "message": "OK",
                }
            ]
        }
    }

class Created(BaseModel):
    message: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "message": "Created",
                }
            ]
        }
    }

class BadRequest(BaseModel):
    message: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "message": "Bad Request",
                }
            ]
        }
    }

class Unauthorized(BaseModel):
    message: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "message": "Unauthorized",
                }
            ]
        }
    }

class NotFound(BaseModel):
    message: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "message": "Not Found",
                }
            ]
        }
    }

class InternalServerError(BaseModel):
    message: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "message": "Internal Server Error",
                }
            ]
        }
    }
