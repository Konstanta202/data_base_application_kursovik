from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship, MappedColumn
from data_base_application_kursovik.Kursovik.DB.Core.base import Base
from data_base_application_kursovik.Kursovik.DB.Models.departments import Departments
from data_base_application_kursovik.Kursovik.DB.Models.employees import Employees
class DepartmentsEmployees(Base):
    __tablename__ = 'departments_employees'
    id: Mapped[int] = mapped_column(primary_key=True)
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id", ondelete="CASCADE"))
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id", ondelete="CASCADE"))

    __table_args__ = (UniqueConstraint("department_id", "employee_id", name="uq_department_employee"),)

    repr_cols = ['id', 'department_id', 'employee_id']