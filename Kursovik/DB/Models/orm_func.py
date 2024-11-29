from typing import Optional
from data_base_application_kursovik.Kursovik.DB.Core.CoreMainDB import sync_engine, session_factory
from data_base_application_kursovik.Kursovik.DB.Core.base import Base
from sqlalchemy import select, update, func, cast, Integer, String, and_, delete, extract
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import aliased, joinedload, selectinload, contains_eager, joinedload
from data_base_application_kursovik.Kursovik.DB.Models.projects import Projects
from data_base_application_kursovik.Kursovik.DB.Models.departments import Departments
from data_base_application_kursovik.Kursovik.DB.Models.employees import Employees
from data_base_application_kursovik.Kursovik.DB.Models.departments_employees import DepartmentsEmployees
import datetime
import bcrypt
from data_base_application_kursovik.Kursovik.DB.Models.users import Users


class OrmFunc:
    @staticmethod
    def create_tables():
        sync_engine.echo = False
        # Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = False

    @staticmethod
    def create_user(user_name: str, password: str, mode: str = 'user'):
        with session_factory() as session:
            user_name_hash = bcrypt.hashpw(user_name.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            user = Users(user_name=user_name_hash, password=password_hash, mode=mode)
            session.add(user)
            session.commit()
    @staticmethod
    def select_user_mode(user_name: str) -> str:
        with session_factory() as session:
            users = session.execute(select(Users)).scalars().all()
            for user in users:
                if bcrypt.checkpw(user_name.encode('utf-8'), user.user_name.encode('utf-8')):
                    return user.mode
            return None
    @staticmethod
    def create_employees(first_name:str, father_name:str, last_name:str, position:str, salary:float):
        with session_factory() as session:
            employees = Employees(first_name=first_name, father_name=father_name,
                                  last_name=last_name, position=position, salary=salary)
            session.add(employees)
            session.commit()

    @staticmethod
    def create_departments(name: str):
        with session_factory() as session:
            departments = Departments(name=name)
            session.add(departments)
            session.commit()

    @staticmethod
    def create_departments_employees(departments:int, employees:int):
        # try:
            with session_factory() as session:
                departments_employees = DepartmentsEmployees(department_id=departments, employee_id=employees)
                session.add(departments_employees)
                session.commit()
        # except Exception as e:
        #     session.rollback()
        #     print("This employee has in this department")

    @staticmethod
    def create_projects(name: str, cost: float, department: Optional[int],
                        date_beg: Optional[datetime.date], date_end: Optional[datetime.date],
                        date_real_end: Optional[datetime.date]):
        # try:
            with session_factory() as session:  # Создаем сессию
                projects = Projects(
                    name=name,
                    cost=cost,
                    department_id=department,
                    date_beg=date_beg,
                    date_end=date_end,
                    date_real_end=date_real_end
                )
                session.add(projects)  # Добавляем объект
                session.commit()  # Фиксируем изменения
        # except IntegrityError as e:
        #     session.rollback()
        #     print("Incorrect create projects, need write date_beg")
        # except ValueError as e:
        #     session.rollback()
        #     print(e.args)

    @staticmethod
    def check_user_exists(user_name: str, password: str) -> bool:
        with session_factory() as session:
            users = session.execute(select(Users)).scalars().all()
            for user in users:
                if user.check_password(password) and bcrypt.checkpw(user_name.encode('utf-8'), user.user_name.encode('utf-8')):
                    return True
            return False

    @staticmethod
    def select_all_projects() -> list:
        with session_factory() as session:
            res = session.execute(select(Projects)).scalars().all()
            return res

    @staticmethod
    def select_all_employees() -> list:
        with session_factory() as session:
            res = session.execute(select(Employees)).scalars().all()
            return res

    @staticmethod
    def select_all_departments() -> list:
        with session_factory()as session:
            res = session.execute(select(Departments)).scalars().all()
            return res

    @staticmethod
    def select_all_departments_employees() -> list:
        with session_factory() as session:
            res = session.execute(select(DepartmentsEmployees)).scalars().all()
            return res
    @staticmethod
    def return_projects():
        with session_factory() as session:
            projects = session.execute(select(Projects)).scalars().all()
            return projects

    @staticmethod
    def update_date_real_end(project_id: int, date_real_end: datetime.date):
        with session_factory() as session:
            query = select(Projects).where(Projects.id == project_id)
            result = session.execute(query)
            # try:
            # project = result.scalar_one()  # Получаем единственный результат
            project = result.scalar_one_or_none()
            if project is None:
                raise TypeError()
            project.date_real_end = date_real_end  # Обновляем дату окончания
            session.commit()  # Сохраняем изменения в базе данных
            # except Exception:
            #     print(f"Project not found.")

    @staticmethod
    def update_date_end(project_id: int, date_end: datetime.date):
        with session_factory() as session:
            query = select(Projects).where(Projects.id == project_id)
            result = session.execute(query)
            # try:
            project = result.scalar_one()
            project.date_end = date_end
            session.commit()
            # except Exception:
            #     print(f"Project not found.")
    @staticmethod
    def update_name_project(id: int, new_name: str):
        with session_factory() as session:
            query = select(Projects).where(Projects.id == id)
            result = session.execute(query)
            # try:
            project = result.scalar_one_or_none()
            if project is None:
                raise TypeError()
            project.name = new_name
            session.commit()
            # except Exception:
            #     print(f"Project not found.")
    @staticmethod
    def update_department_project(priject_id: int, department_id: int):
        with session_factory() as session:
            query = select(Projects).where(Projects.id == priject_id)
            result = session.execute(query)
            # try:
            department = session.execute(select(Projects).where(Departments.id == department_id)).scalar_one_or_none()
            project = result.scalar_one_or_none()
            if project is None or department is None:
                raise TypeError()
            project.department_id = department_id
            session.commit()

            # except Exception:
            #     print(f"Department not found.")

    @staticmethod
    def update_employees_departments(departments: int, employee_old: int, employee_new: int):
        # try:
            with session_factory() as session:
                departments_employees = session.get(DepartmentsEmployees, departments, employee_old).scalar_one_or_none()
                if departments_employees is None:
                    raise TypeError()
                departments_employees.employee_id = employee_new
                session.refresh(departments_employees)
                session.commit()
        # except Exception as e:
        #     session.rollback()
            # print("This employee has in this department")

    @staticmethod
    def update_name_department(id: int, new_name: str):
        with session_factory() as session:
            query = select(Departments).where(Departments.id == id)
            result = session.execute(query)
            # try:
            department = result.scalar_one_or_none()
            if department is None:
                raise TypeError()
            department.name = new_name
            session.commit()
            # except Exception:
            #     print(f"Department not found.")


    @staticmethod
    def update_FFL_employees(id: int, new_first_name: str, new_father_name, new_last_name: str):
        with session_factory() as session:
            query = select(Employees).where(Employees.id == id)
            result = session.execute(query)
            # try:
            employees = result.scalar_one_or_none()
            if employees is None:
                raise TypeError()
            employees.first_name = new_first_name
            employees.father_name = new_father_name
            employees.last_name = new_last_name
            session.commit()
            # except Exception:
            #     print(f"Employees not found.")

    @staticmethod
    def update_salary_employees(employee_id: int, salary: float):
        with session_factory() as session:
            query = select(Employees).where(Employees.id == employee_id)
            result = session.execute(query)
            # try:
            employees = result.scalar_one_or_none()
            if employees is None:
                raise TypeError()
            employees.salary = salary
            session.commit()
            # except Exception:
            #     print(f'Employees not found')

    @staticmethod
    def update_position_employees(employee_id: int, position: str):
        with session_factory() as session:
            query = select(Employees).where(Employees.id == employee_id)
            result = session.execute(query)
            # try:
            employees = result.scalar_one_or_none()
            if employees is None:
                raise TypeError()
            employees.position = position
            session.commit()
            # except Exception:
            #     print(f'Employees not found')

    @staticmethod
    def delete_project(project_id: int):
        with session_factory() as session:
            stmt = select(Projects).where(Projects.id == project_id)
            res = session.execute(stmt)
            projects = res.scalar_one_or_none()
            if projects is None:
                raise TypeError()
            del_p = delete(Projects).where(Projects.id == project_id)
            session.execute(del_p)
            session.commit()

    @staticmethod
    def delete_department_employee(department: int, employee_id: int):
        with session_factory() as session:
            query = (
                select(DepartmentsEmployees)
                .filter(and_(
                    DepartmentsEmployees.department_id == department,
                    DepartmentsEmployees.employee_id == employee_id
                ))
            )

            res = session.execute(query).scalar_one_or_none()

            if res is None:
                raise TypeError()
            stmt = delete(DepartmentsEmployees).filter(and_(DepartmentsEmployees.department_id == department,
                                                            DepartmentsEmployees.employee_id == employee_id))
            session.execute(stmt)
            session.commit()

    @staticmethod
    def delete_department(department_id: int):
        with session_factory() as session:
            query = select(Departments).where(Departments.id == department_id)
            res = session.execute(query).scalar_one_or_none()
            if res is None:
                raise TypeError()
            stmt = delete(Departments).where(Departments.id == department_id)
            session.execute(stmt)
            session.commit()

    @staticmethod
    def delete_empoyee(employee: int):
        with session_factory() as session:
            query = select(Employees).where(Employees.id == employee)
            res = session.execute(query).scalar_one_or_none()
            if res is None:
                raise TypeError()
            stmt = delete(Employees).where(Employees.id == employee)
            session.execute(stmt)
            session.commit()

    @staticmethod
    def calculate_projects_cost() -> list:
        with session_factory() as session:
            departments_alias = aliased(Departments)
            employees_alias = aliased(Employees)
            departments_employees_alias = aliased(DepartmentsEmployees)

            # Формируем запрос
            query = (
                session.query(
                    Projects.name.label("project_name"),
                    (Projects.cost - func.sum(
                        employees_alias.salary *
                        (
                                (extract('year', func.age(Projects.date_real_end, Projects.date_beg)) * 12) +
                                extract('month', func.age(Projects.date_real_end, Projects.date_beg))
                        )
                    )).label("profit")
                )
                .join(departments_alias, Projects.department_id == departments_alias.id)
                .join(departments_employees_alias, departments_alias.id == departments_employees_alias.department_id)
                .join(employees_alias, departments_employees_alias.employee_id == employees_alias.id)
                .filter(Projects.date_beg.isnot(None))  # WHERE projects.date_beg IS NOT NULL
                .group_by(Projects.name, Projects.cost)  # GROUP BY projects.name, projects.cost
            )

            # Выполнение запроса
            results = query.all()
            print()
            return results
