from typing import Optional, Annotated

from jsonschema.validators import validates
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates
from data_base_application_kursovik.Kursovik.DB.Core.base import Base, str_256
from datetime import datetime

class Projects(Base):
    __tablename__ = 'projects'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    cost: Mapped[float] = mapped_column()
    department_id: Mapped[Optional[int]] = mapped_column(ForeignKey('departments.id', ondelete="SET NULL"), nullable=True)
    date_beg: Mapped[Optional[datetime.date]] = mapped_column(Date, nullable=False)
    date_end: Mapped[Optional[datetime.date]] = mapped_column(Date, nullable=True)
    date_real_end: Mapped[Optional[datetime.date]] = mapped_column(Date, nullable=True)


    @validates('date_beg')
    def validate_date_beg(self, key, value: datetime.date):
        if self.date_end is not None and value > self.date_end:
            raise ValueError("date_beg must be less than date_end")
        if self.date_real_end is not None and value > self.date_real_end:
            raise ValueError("date_beg must be less than date_real_end")
        return value

    @validates('date_end')
    def validate_date_end(self, key, value: datetime.date):
        if value is not None and self.date_beg > value:
            raise ValueError("date_end must be greater than date_beg")
        return value

    @validates('date_real_end')
    def validate_date_real_end(self, key, value: datetime.date):
        if value is not None and self.date_beg > value:
            raise ValueError("date_real_end must be greater than date_beg")
        return value

    repr_cols = ['id', 'name', 'cost', 'date_beg', 'date_end', 'date_real_end']