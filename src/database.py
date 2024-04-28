from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config

DATABASE_URL = "{}://{}:{}@{}:{}/{}?charset={}".format(
    "mysql+pymysql",
    config.settings.mysql_user,
    config.settings.mysql_password,
    "db",
    "3306",
    config.settings.mysql_database,
    "utf8mb4"
)

Engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

Base = declarative_base()