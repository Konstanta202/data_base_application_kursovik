from typing import Optional, Annotated
from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data_base_application_kursovik.Kursovik.DB.Core.base import Base, str_256

str_col = Annotated[str, String(256)]
class Employees(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key = True)
    first_name: Mapped[str]
    father_name: Mapped[str]
    last_name: Mapped[str]
    position: Mapped[str]
    salary: Mapped[float]

    repr_cols = ['id', 'first_name', 'father_name', 'last_name', 'position', 'salary']
