import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QComboBox
)
from data_base_application_kursovik.Kursovik.DB.Models.orm_func import OrmFunc

class RegistrationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("REGISTRATION")
        self.setGeometry(150, 150, 300, 150)

        # Центральный виджет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Элементы интерфейса
        self.login_label = QLabel("Login:")
        self.login_input = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)


        self.register_button = QPushButton("REGISTRATION")

        # Верстка
        layout = QVBoxLayout()
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.register_button)

        self.central_widget.setLayout(layout)

        # Связывание кнопки с действием
        self.register_button.clicked.connect(self.register_user)

    def register_user(self):
        login = self.login_input.text()
        password = self.password_input.text()
        if not login or not password:
            QMessageBox.warning(self, "Error", "Please, input login or password!")
            return
        if OrmFunc.check_user_exists(login, password) is False:
            OrmFunc.create_user(login, password)
            QMessageBox.information(self, "Information", "Create new user")
        else:
            QMessageBox.information(self, "Information", "User already exists")
        self.close()