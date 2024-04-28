from pydantic import BaseModel, Field

class OK(BaseModel):
    message: str = Field(example="OK")

class Created(BaseModel):
    message: str = Field(example="Created")

class BadRequest(BaseModel):
    message: str = Field(example="Bad Request")

class Unauthorized(BaseModel):
    message: str = Field(example="Unauthorized")

class NotFound(BaseModel):
    message: str = Field(example="Not Found")

class InternalServerError(BaseModel):
    message: str = Field(example="Internal Server Error")
