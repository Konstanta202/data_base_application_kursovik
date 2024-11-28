import sys

from data_base_application_kursovik.Kursovik.GUI.admin_window import AdminInterface
from data_base_application_kursovik.Kursovik.GUI.registration_window import RegistrationWindow
from data_base_application_kursovik.Kursovik.GUI.user_window import UserInterface

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QComboBox
)
from data_base_application_kursovik.Kursovik.DB.Models.orm_func import OrmFunc


class LoginWindow(QMainWindow):
    open_main_window = False
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AUTORIZATION")
        self.setGeometry(100, 100, 300, 200)

        # Центральный виджет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Элементы интерфейса
        self.login_label = QLabel("Login:")
        self.login_input = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Sig in")
        self.register_button = QPushButton("Registration")
        # Верстка
        layout = QVBoxLayout()
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        self.central_widget.setLayout(layout)

        # Связывание кнопок с действиями
        self.login_button.clicked.connect(self.check_login)
        self.register_button.clicked.connect(self.open_registration_window)

    def check_login(self):
        login = self.login_input.text()
        password = self.password_input.text()
        if OrmFunc.check_user_exists(login, password) is False:
            QMessageBox.information(self, "ERROR", "Incorrect input login or password")
        else:
            QMessageBox.information(self, "INFORMATION", "You successfully logged")
            if OrmFunc.select_user_mode(login) == 'admin':
                self.open_admin_window()
            else:
                self.open_user_window()
            self.close()

    def open_registration_window(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.show()

    def open_user_window(self):
        self.main_window = UserInterface()
        self.main_window.show()

    def open_admin_window(self):
        self.admin_window = AdminInterface()
        self.admin_window.show()