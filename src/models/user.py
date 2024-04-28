from sqlalchemy import (
    UniqueConstraint,
    Column,
    BigInteger,
    String,
    DateTime,
    event,
    orm
)
from sqlalchemy.orm import Session
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = (UniqueConstraint('email','deleted_at'),{})

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    uid = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(255), index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)
    deleted_at = Column(DateTime)

@event.listens_for(Session, "do_orm_execute")
def _add_filtering_deleted_at(execute_state):
    """
    論理削除用のfilterを自動的に適用する
    以下のようにすると、論理削除済のデータも含めて取得可能
    query(...).filter(...).execution_options(include_deleted=True)
    """
    if (
        execute_state.is_select
        and not execute_state.is_column_load
        and not execute_state.is_relationship_load
        and not execute_state.execution_options.get("include_deleted", False)
    ):
        execute_state.statement = execute_state.statement.options(
            orm.with_loader_criteria(
                User,
                lambda cls: cls.deleted_at.is_(None),
                include_aliases=True,
            )
        )