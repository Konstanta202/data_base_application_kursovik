from data_base_application_kursovik.Kursovik.DB.Models.orm_func import OrmFunc
from datetime import datetime

class CreateTableData:
    @staticmethod
    def create_emplloyees():
        OrmFunc.create_employees("Ivan", "Alekseevich", "Semenov", "manager", 1000.00)
        OrmFunc.create_employees("Kiril", "Alekseevich", "Smith", "designer", 1200.00)
        OrmFunc.create_employees("Yarik", "Petrov", "Mazilov", "engineer", 1000.00)
        OrmFunc.create_employees("Maria", "Ivanovna", "Ivanova", "cleaner", 1000.00)
        OrmFunc.create_employees("Aleksey", "Victorovich", "Karlnosov", "developer", 2000.00)
        OrmFunc.create_employees("Dmitriy", "Konstantinovich", "Mishystin", "tester", 1500.00)
        OrmFunc.create_employees("Roman", "Eugenivich", "Bobrikov", "developer", 2000.00)
        OrmFunc.create_employees("Nikita", "Michaelivich", "Fusar", "Qa engineer", 2500.00)

    @staticmethod
    def create_departments():
        OrmFunc.create_departments("Creanatory")
        OrmFunc.create_departments("Develop")
        OrmFunc.create_departments("Advetrising")
        OrmFunc.create_departments("Design")
        OrmFunc.create_departments("Super Paper")
        OrmFunc.create_departments("Data Analitics")

    @staticmethod
    def create_department_employees():
        OrmFunc.create_departments_employees(2,5)
        OrmFunc.create_departments_employees(2,1)
        OrmFunc.create_departments_employees(1,2)
        OrmFunc.create_departments_employees(3,4)
        OrmFunc.create_departments_employees(4,2)
        OrmFunc.create_departments_employees(6,8)
        OrmFunc.create_departments_employees(6,1)
        OrmFunc.create_departments_employees(6,4)

    @staticmethod
    def create_projects():
        OrmFunc.create_projects("Adverticing = coffe", 50000.00,
                                3,
                                CreateTableData.convert_date("2024-07-15"),
                                CreateTableData.convert_date("2024-09-15"),
                                CreateTableData.convert_date("2024-11-21"))

        OrmFunc.create_projects("Design wabpage", 60000.00,
                                4,
                                CreateTableData.convert_date("2024-08-15"),
                                CreateTableData.convert_date("2024-09-30"),
                                CreateTableData.convert_date("2024-10-14"))

        OrmFunc.create_projects("Math application", 120000.00,
                                2,
                                CreateTableData.convert_date("2024-07-15"),
                                CreateTableData.convert_date("2024-09-15"),
                                CreateTableData.convert_date("2024-11-21"))

        OrmFunc.create_projects("Hand Made Shop", 300000.00,
                                3,
                                CreateTableData.convert_date("2024-03-20"),
                                CreateTableData.convert_date("2024-09-30"),
                                CreateTableData.convert_date("2024-10-20"))

        OrmFunc.create_projects("Buisness Application", 350000.00,
                                3,
                                CreateTableData.convert_date("2024-03-15"),
                                CreateTableData.convert_date("2024-07-21"),
                                CreateTableData.convert_date("2024-08-10"))

        OrmFunc.create_projects("Soft for buisness logic", 50000.00,
                                3,
                                CreateTableData.convert_date("2024-08-20"),
                                CreateTableData.convert_date("2024-10-21"),
                                CreateTableData.convert_date("2024-12-10"))

    @staticmethod
    def convert_date(date: str):
        return datetime.strptime(date, "%Y-%m-%d").date()
