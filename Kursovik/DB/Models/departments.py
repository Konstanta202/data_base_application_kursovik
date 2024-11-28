from typing import Optional, Annotated
from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship, MappedColumn
from Kursovik.DB.Core.base import Base, str_256
from datetime import datetime

class Departments(Base):
    __tablename__ = 'departments'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


    repr_cols = ['id', 'name']