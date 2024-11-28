from data_base_application_kursovik.Kursovik.DB.Models.orm_func import OrmFunc
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
                             QVBoxLayout, QWidget, QPushButton, QLabel, QSpacerItem, QSizePolicy, QHBoxLayout)
from PyQt5.QtCore import Qt

class UserInterface(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Interface")
        self.setGeometry(100, 100, 600, 300)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        top_layout = QHBoxLayout()
        main_layout.addLayout(top_layout)

        self.top_left_button = QPushButton("Exit")
        self.top_left_button.clicked.connect(self.un_login)
        top_layout.addWidget(self.top_left_button, alignment=Qt.AlignLeft)

        top_layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.layout = QVBoxLayout()
        main_layout.addLayout(self.layout)

        self.create_main_screen()
    def un_login(self):
        self.close()

    def create_main_screen(self):
        self.layout.addWidget(QLabel("Welcome User:", alignment=Qt.AlignCenter))
        self.layout.addWidget(QLabel("Select Table:", alignment=Qt.AlignCenter))

        btn_table1 = QPushButton("Projects")
        btn_table1.clicked.connect(lambda: self.show_projects())
        self.layout.addWidget(btn_table1)

        btn_table2 = QPushButton("Profit")
        btn_table2.clicked.connect(lambda: self.show_profit_projects())
        self.layout.addWidget(btn_table2)

        btn_table3 = QPushButton("Employees")
        btn_table3.clicked.connect(lambda: self.show_employees())
        self.layout.addWidget(btn_table3)

        btn_table4 = QPushButton("Departments")
        btn_table4.clicked.connect(lambda: self.show_departments())
        self.layout.addWidget(btn_table4)

        btn_table4 = QPushButton("Departments_empoyees")
        btn_table4.clicked.connect(lambda: self.show_department_employees())
        self.layout.addWidget(btn_table4)

    def clear_layout(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()
    def create_table_widget(self, row_count, column_count, headers):

        table_widget = QTableWidget()
        table_widget.setRowCount(row_count)
        table_widget.setColumnCount(column_count)
        table_widget.setHorizontalHeaderLabels(headers)
        return table_widget

    def add_back_button(self):
        btn_back = QPushButton("Back")
        btn_back.clicked.connect(self.back_to_main)
        self.layout.addWidget(btn_back)
    def show_projects(self):
        self.clear_layout()
        projects = OrmFunc.return_projects()
        table_widget = self.create_table_widget(len(projects), 7,["ID", "Name", "Cost", "Department", "date_beg",
                                                     "date_end", "date_real_end"])
        # Заполняем таблицу
        for row_index, project in enumerate(projects):
            table_widget.setItem(row_index, 0, QTableWidgetItem(str(project.id)))
            table_widget.setItem(row_index, 1, QTableWidgetItem(project.name))
            table_widget.setItem(row_index, 2, QTableWidgetItem(str(project.cost)))
            table_widget.setItem(row_index, 3, QTableWidgetItem(str(project.department_id)))
            table_widget.setItem(row_index, 4, QTableWidgetItem(str(project.date_beg)))
            table_widget.setItem(row_index, 5, QTableWidgetItem(str(project.date_end)))
            table_widget.setItem(row_index, 6, QTableWidgetItem(str(project.date_real_end)))

        self.layout.addWidget(table_widget)
        self.add_back_button()

    def show_profit_projects(self):
        self.clear_layout()
        profit = OrmFunc.calculate_projects_cost()
        table_widget = self.create_table_widget(len(profit), 2, ["Name", "Profit"])

        for row_index, project in enumerate(profit):
            table_widget.setItem(row_index, 0, QTableWidgetItem(str(project[0])))
            table_widget.setItem(row_index, 1, QTableWidgetItem(str(project[1])))

        self.layout.addWidget(table_widget)
        self.add_back_button()
    def show_employees(self):
        self.clear_layout()
        employees = OrmFunc.select_all_employees()
        table_widget = self.create_table_widget(len(employees), 6, ["Id", "First Name", "Father Name",
                                                                    "Last Name", "Position", "Salary"])
        for row_index, employee in enumerate(employees):
            table_widget.setItem(row_index, 0, QTableWidgetItem(str(employee.id)))
            table_widget.setItem(row_index, 1, QTableWidgetItem(str(employee.first_name)))
            table_widget.setItem(row_index, 2, QTableWidgetItem(str(employee.father_name)))
            table_widget.setItem(row_index, 3, QTableWidgetItem(str(employee.last_name)))
            table_widget.setItem(row_index, 4, QTableWidgetItem(str(employee.position)))
            table_widget.setItem(row_index, 5, QTableWidgetItem(str(employee.salary)))

        self.layout.addWidget(table_widget)
        self.add_back_button()

    def show_departments(self):
        self.clear_layout()
        departments = OrmFunc.select_all_departments()
        table_widget = self.create_table_widget(len(departments), 2,["Id", "Department"])

        for row_index, department in enumerate(departments):
            table_widget.setItem(row_index, 0, QTableWidgetItem(str(department.id)))
            table_widget.setItem(row_index, 1, QTableWidgetItem(str(department.name)))
        self.layout.addWidget(table_widget)
        self.add_back_button()

    def show_department_employees(self):
        self.clear_layout()
        department_employees = OrmFunc.select_all_departments_employees()
        table_widget = self.create_table_widget(len(department_employees),3,["Id", "Department_id", "Employee_id"])

        for row_index, department_empl in enumerate(department_employees):
            table_widget.setItem(row_index, 0, QTableWidgetItem(str(department_empl.id)))
            table_widget.setItem(row_index, 1, QTableWidgetItem(str(department_empl.department_id)))
            table_widget.setItem(row_index, 2, QTableWidgetItem(str(department_empl.employee_id)))

        self.layout.addWidget(table_widget)
        self.add_back_button()

    def back_to_main(self):
        # Очистить текущий вид
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Вернуться к главному экрану
        self.create_main_screen()
