from typing import Optional, Annotated
from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data_base_application_kursovik.Kursovik.DB.Core.base import Base, metadata_obj, str_256
import enum, datetime
import bcrypt

class Users(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    mode: Mapped[str] = mapped_column(String, nullable=False)

    def set_password(self, password: str) -> None:
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt)
    def set_username(self, user_name: str) -> None:
        self.user_name = bcrypt.hashpw(user_name.encode('utf-8'), bcrypt)

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

    def check_username(self, user_name: str) -> bool:
        return bcrypt.checkpw(user_name.encode('utf-8'), self.user_name.encode('utf-8'))



