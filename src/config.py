from pydantic_settings import BaseSettings
 
class Settings(BaseSettings):
    env: str
    tz: str
    mysql_database: str
    mysql_user: str
    mysql_password: str
    mysql_root_password: str

settings = Settings()