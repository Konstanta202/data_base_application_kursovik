from sqlite3 import IntegrityError

from data_base_application_kursovik.Kursovik.DB.Models.orm_func import OrmFunc
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
                             QVBoxLayout, QWidget, QPushButton, QLabel, QSpacerItem, QSizePolicy, QHBoxLayout,
                             QLineEdit, QMessageBox)
from PyQt5.QtCore import Qt
from datetime import datetime

class AdminInterface(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ADMIN Interface")
        self.setGeometry(100, 100, 600, 300)

        # Основной макет
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Верхний макет с кнопкой в левом верхнем углу
        top_layout = QHBoxLayout()
        main_layout.addLayout(top_layout)

        # Кнопка в левом верхнем углу
        self.top_left_button = QPushButton("Exit")
        self.top_left_button.clicked.connect(self.un_login)
        top_layout.addWidget(self.top_left_button, alignment=Qt.AlignLeft)

        # Распорка для выравнивания остального контента
        top_layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Основной контент (ниже кнопки)
        self.layout = QVBoxLayout()
        main_layout.addLayout(self.layout)
        self.create_main_screen()


    def un_login(self):
            self.close()

    def create_main_screen(self):
        self.setGeometry(100, 100, 600, 300)
        self.layout.addWidget(QLabel("Welcome Admin:", alignment=Qt.AlignCenter))
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
        while self.layout.count():
            item = self.layout.takeAt(0)
            if isinstance(item, QVBoxLayout) or isinstance(item, QHBoxLayout):
                # Рекурсивно очищаем вложенные макеты
                self.clear_nested_layout(item)
            elif item.widget():
                # Удаляем виджет
                item.widget().deleteLater()

    def clear_nested_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if isinstance(item, QVBoxLayout) or isinstance(item, QHBoxLayout):
                # Рекурсивно очищаем вложенные макеты
                self.clear_nested_layout(item)
            elif item.widget():
                # Удаляем виджет
                item.widget().deleteLater()

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

        button_layout = QHBoxLayout()
        self.setGeometry(100,100,1000,600)

        # Кнопка "Create project"
        add_project_button = QPushButton("Create project")
        add_project_button.clicked.connect(self.add_project_form)
        button_layout.addWidget(add_project_button)

        # Кнопка "Update name"
        add_project_button1 = QPushButton("Update name")
        add_project_button1.clicked.connect(self.update_name_project)  # Пример действия
        button_layout.addWidget(add_project_button1)

        add_project_button0 = QPushButton("Set department")
        add_project_button0.clicked.connect(self.set_project_department)  # Пример действия
        button_layout.addWidget(add_project_button0)

        add_project_button2 = QPushButton("Update date end")
        add_project_button2.clicked.connect(self.update_date_end)  # Пример действия
        button_layout.addWidget(add_project_button2)

        add_project_button3 = QPushButton("Update date real end")
        add_project_button3.clicked.connect(self.update_date_real_end)  # Пример действия
        button_layout.addWidget(add_project_button3)

        add_project_button4 = QPushButton("Delete project")
        add_project_button4.clicked.connect(self.delete_project)  # Пример действия
        button_layout.addWidget(add_project_button4)

        # Добавляем горизонтальный макет в основной вертикальный макет
        self.layout.addLayout(button_layout)


        table_widget = self.create_table_widget(len(projects), 7, ["ID", "Name", "Cost", "Department", "date_beg",
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
        self.setGeometry(100,100,1000,600)
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
        self.setGeometry(100,100,1000,600)

        button_layout = QHBoxLayout()

        add_project_button = QPushButton("Create employee")
        add_project_button.clicked.connect(self.create_employee)
        button_layout.addWidget(add_project_button)

        add_project_button1 = QPushButton("Update salary")
        add_project_button1.clicked.connect(self.update_salary)  # Пример действия
        button_layout.addWidget(add_project_button1)

        add_project_button2 = QPushButton("Update position")
        add_project_button2.clicked.connect(self.update_position)  # Пример действия
        button_layout.addWidget(add_project_button2)

        add_project_button2 = QPushButton("Delete employee")
        add_project_button2.clicked.connect(self.delete_employee)  # Пример действия
        button_layout.addWidget(add_project_button2)

        # Добавляем горизонтальный макет в основной вертикальный макет
        self.layout.addLayout(button_layout)

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
        self.setGeometry(100,100,1000,600)

        button_layout = QHBoxLayout()

        add_project_button = QPushButton("Create department")
        add_project_button.clicked.connect(self.create_department)
        button_layout.addWidget(add_project_button)


        add_project_button = QPushButton("Update name")
        add_project_button.clicked.connect(self.update_name_department)
        button_layout.addWidget(add_project_button)

        add_project_button = QPushButton("Delete department")
        add_project_button.clicked.connect(self.delete_department)
        button_layout.addWidget(add_project_button)

        self.layout.addLayout(button_layout)


        table_widget = self.create_table_widget(len(departments), 2, ["Id", "Department"])

        for row_index, department in enumerate(departments):
            table_widget.setItem(row_index, 0, QTableWidgetItem(str(department.id)))
            table_widget.setItem(row_index, 1, QTableWidgetItem(str(department.name)))
        self.layout.addWidget(table_widget)
        self.add_back_button()

    def show_department_employees(self):
        self.clear_layout()
        self.setGeometry(100,100,1000,600)
        department_employees = OrmFunc.select_all_departments_employees()
        table_widget = self.create_table_widget(len(department_employees), 3, ["Id", "Department_id", "Employee_id"])
        button_layout = QHBoxLayout()

        add_project_button = QPushButton("Create department_employee")
        add_project_button.clicked.connect(self.create_department_employee)
        button_layout.addWidget(add_project_button)


        add_project_button = QPushButton("Set new employee")
        add_project_button.clicked.connect(self.update_name_department_employee)
        button_layout.addWidget(add_project_button)

        add_project_button = QPushButton("Delete department_employee")
        add_project_button.clicked.connect(self.delete_department_employee)
        button_layout.addWidget(add_project_button)

        self.layout.addLayout(button_layout)

        for row_index, department_empl in enumerate(department_employees):
            table_widget.setItem(row_index, 0, QTableWidgetItem(str(department_empl.id)))
            table_widget.setItem(row_index, 1, QTableWidgetItem(str(department_empl.department_id)))
            table_widget.setItem(row_index, 2, QTableWidgetItem(str(department_empl.employee_id)))

        self.layout.addWidget(table_widget)
        self.add_back_button()

    def back_to_main(self):
        # # Очистить текущий вид
        # for i in reversed(range(self.layout.count())):
        #     widget = self.layout.itemAt(i).widget()
        #     if widget:
        #         widget.deleteLater()
        self.clear_nested_layout(self.layout)


        # Вернуться к главному экрану
        self.create_main_screen()

    def add_project_form(self):
        self.clear_layout()
        # Поля для ввода данных
        input_name = QLineEdit()
        self.layout.addWidget(QLabel("Project Name:"))
        self.layout.addWidget(input_name)

        input_cost = QLineEdit()
        self.layout.addWidget(QLabel("Cost:"))
        self.layout.addWidget(input_cost)

        input_department = QLineEdit()
        self.layout.addWidget(QLabel("Department id:"))
        self.layout.addWidget(input_department)

        input_date_beg = QLineEdit()
        self.layout.addWidget(QLabel("Date begin:"))
        self.layout.addWidget(input_date_beg)

        input_date_end = QLineEdit()
        self.layout.addWidget(QLabel("Date end:"))
        self.layout.addWidget(input_date_end)

        input_date_real_end = QLineEdit()
        self.layout.addWidget(QLabel("Date real end:"))
        self.layout.addWidget(input_date_real_end)

        btn_submit = QPushButton("Create project")
        self.layout.addWidget(btn_submit, alignment=Qt.AlignCenter)

        # Обработчик нажатия на кнопку
        def handle_submit():
            name = input_name.text().strip()
            cost = input_cost.text().strip()
            department_id = input_department.text().strip()
            date_beg = input_date_beg.text().strip()
            date_end = input_date_end.text().strip()
            date_real_end = input_date_real_end.text().strip()

            # Проверяем корректность данных
            if not name or not cost.isdigit() or not  date_beg:
                error_label = QLabel("Error, incorrect input data!")
                error_label.setStyleSheet("color: red;")
                self.layout.addWidget(error_label)
                return

            department_id = int(department_id) if department_id.isdigit() else None
            date_end = datetime.strptime(date_end, "%Y-%m-%d").date() if date_end else None
            date_real_end = datetime.strptime(date_real_end, "%Y-%m-%d").date() if date_real_end else None

            # Добавляем проект в базу данных
            try:
                OrmFunc.create_projects(
                    name=name,
                    cost=float(cost),
                    department=department_id,
                    date_beg=datetime.strptime(date_beg, "%Y-%m-%d").date(),
                    date_end=date_end,
                    date_real_end=date_real_end
                )
            except IntegrityError as e:
                QMessageBox.information(self, "ERROR", "Incorrect create projects, need write date_beg")
            except ValueError as e:
                QMessageBox.information(self, "ERROR", "Error, please input correct data")

            # Возвращаемся в show_projects
            self.show_projects()
        btn_submit.clicked.connect(handle_submit)
        # Кнопка "Назад"
        self.add_back_button()

    def update_name_project(self):
        self.clear_layout()
        # Поля для ввода данных
        input_id = QLineEdit()
        self.layout.addWidget(QLabel("Project Id:"))
        self.layout.addWidget(input_id)

        input_new_name = QLineEdit()
        self.layout.addWidget(QLabel("New name Project:"))
        self.layout.addWidget(input_new_name)
        btn_submit = QPushButton("Set name")
        self.layout.addWidget(btn_submit, alignment=Qt.AlignCenter)

        # Обработчик нажатия на кнопку
        def handle_submit():
            id = input_id.text().strip()
            new_name = input_new_name.text().strip()

            if not id or not new_name:
                error_label = QLabel("Ошибка: проверьте введённые данные!")
                error_label.setStyleSheet("color: red;")
                self.layout.addWidget(error_label)
                return

            # Добавляем проект в базу данных
            try:
                OrmFunc.update_name_project(int(id), new_name)
            except TypeError:
                QMessageBox.information(self, "ERROR", "Project not found")
                ...

            # Возвращаемся в show_projects
            self.show_projects()
        btn_submit.clicked.connect(handle_submit)
        # Кнопка "Назад"
        self.add_back_button()

    def set_project_department(self):
        self.clear_layout()
        # Поля для ввода данных
        input_id = QLineEdit()
        self.layout.addWidget(QLabel("Project id:"))
        self.layout.addWidget(input_id)

        input_new_name = QLineEdit()
        self.layout.addWidget(QLabel("Department id:"))
        self.layout.addWidget(input_new_name)

        btn_submit = QPushButton("Set department")
        self.layout.addWidget(btn_submit, alignment=Qt.AlignCenter)

        def handle_submit():
                project_id = input_id.text().strip()
                department_id = input_new_name.text().strip()

                if not project_id or not department_id:
                    error_label = QLabel("ERROR: Incorrect input data")
                    error_label.setStyleSheet("color: red;")
                    self.layout.addWidget(error_label)
                    return

                # Добавляем проект в базу данных
                try:
                    OrmFunc.update_department_project(int(project_id), int(department_id))
                except IntegrityError:
                    QMessageBox.information(self, "ERROR", "Incorrect input data_end, we need input data_end more then "
                                                           "date_begin")
                except ValueError:
                    QMessageBox.information(self, "ERROR", "Error, please input correct data")
                except TypeError:
                    QMessageBox.information(self, "ERROR", "Project or department not found")

                self.show_projects()

        btn_submit.clicked.connect(handle_submit)
            # Кнопка "Назад"
        self.add_back_button()


    def update_date_end(self):
            self.clear_layout()
            # Поля для ввода данных
            input_id = QLineEdit()
            self.layout.addWidget(QLabel("Project id:"))
            self.layout.addWidget(input_id)

            input_new_name = QLineEdit()
            self.layout.addWidget(QLabel("Date end:"))
            self.layout.addWidget(input_new_name)

            btn_submit = QPushButton("Update date end")
            self.layout.addWidget(btn_submit, alignment=Qt.AlignCenter)

            def handle_submit():
                id = input_id.text().strip()
                date_end = input_new_name.text().strip()

                if not id or not date_end:
                    error_label = QLabel("Ошибка: проверьте введённые данные!")
                    error_label.setStyleSheet("color: red;")
                    self.layout.addWidget(error_label)
                    return

                # Добавляем проект в базу данных
                try:
                    OrmFunc.update_date_end(int(id), datetime.strptime(date_end, "%Y-%m-%d").date())
                except IntegrityError as e:
                    QMessageBox.information(self, "ERROR", "Incorrect input data_end, we need input data_end more then "
                                                           "date_begin")
                except ValueError as e:
                    QMessageBox.information(self, "ERROR", "Error, please input correct data")

                # Возвращаемся в show_projects
                self.show_projects()
            btn_submit.clicked.connect(handle_submit)
            # Кнопка "Назад"
            self.add_back_button()

    def update_date_real_end(self):
        self.clear_layout()
        # Поля для ввода данных
        input_id = QLineEdit()
        self.layout.addWidget(QLabel("Project id:"))
        self.layout.addWidget(input_id)

        input_new_name = QLineEdit()
        self.layout.addWidget(QLabel("Date end real:"))
        self.layout.addWidget(input_new_name)

        btn_submit = QPushButton("Update date real end")
        self.layout.addWidget(btn_submit, alignment=Qt.AlignCenter)

        def handle_submit():
            id = input_id.text().strip()
            date_real_end = input_new_name.text().strip()

            if not id or not date_real_end:
                error_label = QLabel("Ошибка: проверьте введённые данные!")
                error_label.setStyleSheet("color: red;")
                self.layout.addWidget(error_label)
                return
            try:
                OrmFunc.update_date_real_end(int(id), datetime.strptime(date_real_end, "%Y-%m-%d").date())
            except IntegrityError as e:
                QMessageBox.information(self, "ERROR", "Incorrect input data_real_end, we need input data_real_end more then date_begin")
            except ValueError as e:
                QMessageBox.information(self, "ERROR", "Error, please input correct data")
            except TypeError as e:
                QMessageBox.information(self, "ERROR", "This project not found")
            # Добавляем проект в базу данных
            # OrmFunc.update_date_real_end(int(id), datetime.strptime(date_real_end, "%Y-%m-%d").date())
            # Возвращаемся в show_projects
            self.show_projects()
        btn_submit.clicked.connect(handle_submit)
        # Кнопка "Назад"
        self.add_back_button()

    def delete_project(self):
        self.clear_layout()
        # Поля для ввода данных
        input_id = QLineEdit()
        self.layout.addWidget(QLabel("Project id:"))
        self.layout.addWidget(input_id)

        btn_submit = QPushButton("Delete project")
        self.layout.addWidget(btn_submit, alignment=Qt.AlignCenter)

        def handle_submit():
            id = input_id.text().strip()

            if not id:
                error_label = QLabel("Ошибка: проверьте введённые данные!")
                error_label.setStyleSheet("color: red;")
                self.layout.addWidget(error_label)
                return
            try:
                OrmFunc.delete_project(int(id))
            except TypeError as e:
                    QMessageBox.information(self, "ERROR", "Project not found")
            self.show_projects()
        btn_submit.clicked.connect(handle_submit)

        self.add_back_button()

    def create_employee(self):
        self.clear_layout()
        # Поля для ввода данных
        input_first_name = QLineEdit()
        self.layout.addWidget(QLabel("First name:"))
        self.layout.addWidget(input_first_name)

        input_father_name = QLineEdit()
        self.layout.addWidget(QLabel("Father name:"))
        self.layout.addWidget(input_father_name)

        input_last_name = QLineEdit()
        self.layout.addWidget(QLabel("Last name:"))
        self.layout.addWidget(input_last_name)

        input_position = QLineEdit()
        self.layout.addWidget(QLabel("Position:"))
        self.layout.addWidget(input_position)

        input_salary = QLineEdit()
        self.layout.addWidget(QLabel("Salary:"))
        self.layout.addWidget(input_salary)

        btn_submit = QPushButton("Create employee")
        self.layout.addWidget(btn_submit, alignment=Qt.AlignCenter)

        # Обработчик нажатия на кнопку
        def handle_submit():
            first_name = input_first_name.text().strip()
            father_name = input_father_name.text().strip()
            last_name = input_last_name.text().strip()
            position = input_position.text().strip()
            salary = input_salary.text().strip()

            # Проверяем корректность данных
            if not first_name or not father_name or not last_name or not position or not salary.isdigit():
                error_label = QLabel("Ошибка: проверьте введённые данные!")
                error_label.setStyleSheet("color: red;")
                self.layout.addWidget(error_label)
                return

            # Добавляем проект в базу данных
            OrmFunc.create_employees(
                first_name=first_name,
                father_name=father_name,
                last_name=last_name,
                position=position, salary=float(salary)
            )
            self.show_employees()

        btn_submit.clicked.connect(handle_submit)
        # Кнопка "Назад"
        self.add_back_button()

    def update_salary(self):
        self.clear_layout()
        # Поля для ввода данных
        input_id = QLineEdit()
        self.layout.addWidget(QLabel("Employee id:"))
        self.layout.addWidget(input_id)

        input_salary = QLineEdit()
        self.layout.addWidget(QLabel("New salary:"))
        self.layout.addWidget(input_salary)

        btn_submit = QPushButton("Update salary")
        self.layout.addWidget(btn_submit, alignment=Qt.AlignCenter)

        def handle_submit():
            id = input_id.text().strip()
            salary = input_salary.text().strip()

            if not id or not salary.isdigit():
                error_label = QLabel("Error, incorrect input data!")
                error_label.setStyleSheet("color: red;")
                self.layout.addWidget(error_label)
                return
            try:
                OrmFunc.update_salary_employees(int(id), float(salary))
            except TypeError as e:
                QMessageBox.information(self, "ERROR", "Employee not found")

            self.show_employees()

        btn_submit.clicked.connect(handle_submit)

        self.add_back_button()

    def update_position(self):
        self.clear_layout()
        # Поля для ввода данных
        input_id = QLineEdit()
        self.layout.addWidget(QLabel("Employee id:"))
        self.layout.addWidget(input_id)

        input_position = QLineEdit()
        self.layout.addWidget(QLabel("New Position:"))
        self.layout.addWidget(input_position)

        btn_submit = QPushButton("Update position")
        self.layout.addWidget(btn_submit, alignment=Qt.AlignCenter)

        def handle_submit():
            id = input_id.text().strip()
            position = input_position.text().strip()

            if not id or not position:
                error_label = QLabel("Error, incorrect input data!")
                error_label.setStyleSheet("color: red;")
                self.layout.addWidget(error_label)
                return
            try:
                OrmFunc.update_position_employees(int(id), str(position))
            except TypeError as e:
                QMessageBox.information(self, "ERROR", "Emloyee not found")

            self.show_employees()

        btn_submit.clicked.connect(handle_submit)
        self.add_back_button()

    def delete_employee(self):
        self.clear_layout()
        # Поля для ввода данных
        input_id = QLineEdit()
        self.layout.addWidget(QLabel("Employee id:"))
        self.layout.addWidget(input_id)

        btn_submit = QPushButton("Delete employee")
        self.layout.addWidget(btn_submit, alignment=Qt.AlignCenter)

        def handle_submit():
            id = input_id.text().strip()

            if not id:
                error_label = QLabel("Ошибка: проверьте введённые данные!")
                error_label.setStyleSheet("color: red;")
                self.layout.addWidget(error_label)
                return
            try:
                OrmFunc.delete_empoyee(int(id))
            except TypeError as e:
                QMessageBox.information(self, "ERROR", "Emloyee not found")

            self.show_employees()
        btn_submit.clicked.connect(handle_submit)

        self.add_back_button()

    def create_department(self):
        self.clear_layout()

        input_name = QLineEdit()
        self.layout.addWidget(QLabel("Department name:"))
        self.layout.addWidget(input_name)

        btn_submit = QPushButton("Create new department")
        self.layout.addWidget(btn_submit, alignment=Qt.AlignCenter)

        def handle_submit():
            name_department = input_name.text().strip()

            if not name_department:
                error_label = QLabel("Ошибка: проверьте введённые данные!")
                error_label.setStyleSheet("color: red;")
                self.layout.addWidget(error_label)
                return
            OrmFunc.create_departments(str(name_department))
            self.show_departments()
        btn_submit.clicked.connect(handle_submit)

        self.add_back_button()

    def update_name_department(self):
        self.clear_layout()

        input_id = QLineEdit()
        self.layout.addWidget(QLabel("Department ID:"))
        self.layout.addWidget(input_id)

        input_new_name = QLineEdit()
        self.layout.addWidget(QLabel("Department new name:"))
        self.layout.addWidget(input_new_name)

        btn_submit = QPushButton("Update name department")
        self.layout.addWidget(btn_submit, alignment=Qt.AlignCenter)

        def handle_submit():
            department_id = input_id.text().strip()
            department_name = input_new_name.text().strip()

            if not department_id or not department_name:
                error_label = QLabel("Error: Incorrect input data")
                error_label.setStyleSheet("color: red;")
                self.layout.addWidget(error_label)
                return
            try:
                OrmFunc.update_name_department(int(department_id), str(department_name))
            except TypeError as e:
                QMessageBox.information(self, "ERROR", "Department not found")

            self.show_departments()
        btn_submit.clicked.connect(handle_submit)

        self.add_back_button()

    def delete_department(self):
        self.clear_layout()
        # Поля для ввода данных
        input_id = QLineEdit()
        self.layout.addWidget(QLabel("Department id:"))
        self.layout.addWidget(input_id)

        btn_submit = QPushButton("Delete department")
        self.layout.addWidget(btn_submit, alignment=Qt.AlignCenter)

        def handle_submit():
            id = input_id.text().strip()

            if not id:
                error_label = QLabel("Error: Incorrect input data")
                error_label.setStyleSheet("color: red;")
                self.layout.addWidget(error_label)
                return
            try:
                OrmFunc.delete_department(int(id))
            except TypeError as e:
                QMessageBox.information(self, "ERROR", "Department not found")

            self.show_departments()
        btn_submit.clicked.connect(handle_submit)

        self.add_back_button()

    def create_department_employee(self):
        self.clear_layout()
        # Поля для ввода данных
        input_department_id = QLineEdit()
        self.layout.addWidget(QLabel("Department id:"))
        self.layout.addWidget(input_department_id)

        input_employee_id = QLineEdit()
        self.layout.addWidget(QLabel("Employee id:"))
        self.layout.addWidget(input_employee_id)

        btn_submit = QPushButton("Create department_employee")
        self.layout.addWidget(btn_submit, alignment=Qt.AlignCenter)

        def handle_submit():
            dep_id = input_department_id.text().strip()
            emp_id = input_employee_id.text().strip()

            if not dep_id or not emp_id:
                error_label = QLabel("Error: Incorrect input data")
                error_label.setStyleSheet("color: red;")
                self.layout.addWidget(error_label)
                return
            self.show_department_employees()
            try:
                OrmFunc.create_departments_employees(int(dep_id), int(emp_id))
            except TypeError as e:
                QMessageBox.information(self, "ERROR", "Department not found")

            except Exception as e:
                QMessageBox.information(self, "ERROR", "This employees has department")

        btn_submit.clicked.connect(handle_submit)

        self.add_back_button()

        def create_department_employee(self):
            self.clear_layout()
            # Поля для ввода данных
            input_department_id = QLineEdit()
            self.layout.addWidget(QLabel("Department id:"))
            self.layout.addWidget(input_department_id)

            input_employee_id = QLineEdit()
            self.layout.addWidget(QLabel("Department id:"))
            self.layout.addWidget(input_employee_id)

            btn_submit = QPushButton("Delete department")
            self.layout.addWidget(btn_submit, alignment=Qt.AlignCenter)

            def handle_submit():
                dep_id = input_department_id.text().strip()
                emp_id = input_employee_id.text().strip()

                if not dep_id or not emp_id:
                    error_label = QLabel("Error: Incorrect input data")
                    error_label.setStyleSheet("color: red;")
                    self.layout.addWidget(error_label)
                    return
                self.show_department_employees()
                OrmFunc.create_departments_employees(int(dep_id), int(emp_id))

            btn_submit.clicked.connect(handle_submit)

            self.add_back_button()

    def update_name_department_employee(self):
        self.clear_layout()
        # Поля для ввода данных
        input_department_id = QLineEdit()
        self.layout.addWidget(QLabel("Department id:"))
        self.layout.addWidget(input_department_id)

        input_employee_id_old = QLineEdit()
        self.layout.addWidget(QLabel("Employee old id:"))
        self.layout.addWidget(input_employee_id_old)

        input_employee_id_new = QLineEdit()
        self.layout.addWidget(QLabel("Employee new id:"))
        self.layout.addWidget(input_employee_id_new)



        btn_submit = QPushButton("Delete department")
        self.layout.addWidget(btn_submit, alignment=Qt.AlignCenter)

        def handle_submit():
            dep_id = input_department_id.text().strip()
            emp_id_old = input_employee_id_old.text().strip()
            emp_id_new = input_employee_id_new.text()

            if not dep_id or not emp_id_old or not emp_id_new:
                error_label = QLabel("Error: Incorrect input data")
                error_label.setStyleSheet("color: red;")
                self.layout.addWidget(error_label)
                return
            self.show_department_employees()
            try:
                OrmFunc.update_employees_departments(int(dep_id), int(emp_id_old), int(emp_id_new))
            except TypeError:
                QMessageBox.information(self, "ERROR", "Department or employee not found")

        btn_submit.clicked.connect(handle_submit)

        self.add_back_button()

    def delete_department_employee(self):
        self.clear_layout()
        # Поля для ввода данных
        input_department_id = QLineEdit()
        self.layout.addWidget(QLabel("Department id:"))
        self.layout.addWidget(input_department_id)

        input_employee_id = QLineEdit()
        self.layout.addWidget(QLabel("Employee id:"))
        self.layout.addWidget(input_employee_id)


        btn_submit = QPushButton("Delete department")
        self.layout.addWidget(btn_submit, alignment=Qt.AlignCenter)

        def handle_submit():
            dep_id = input_department_id.text().strip()
            emp_id = input_employee_id.text().strip()

            if not dep_id or not emp_id:
                error_label = QLabel("Error: Incorrect input data")
                error_label.setStyleSheet("color: red;")
                self.layout.addWidget(error_label)
                return
            self.show_department_employees()
            try:
                OrmFunc.delete_department_employee(int(dep_id), int(emp_id))
            except TypeError:
                QMessageBox.information(self, "ERROR", "Department or employee not found")
        btn_submit.clicked.connect(handle_submit)

        self.add_back_button()
