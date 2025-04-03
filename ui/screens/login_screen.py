from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui import css
from utils import *
from typing import *



@singleton
class LoginScreen(QWidget):

    def __init__(self):
        super().__init__()

        self.MAIN_LAYOUT:QLayout = QVBoxLayout(self)

        self.loginContainer:QWidget = QFrame()
        self.loginContainer.setStyleSheet(css.wireframe_style())
        self.loginContainer.setFixedSize(QSize(683, 384))
        self.loginContainer.setContentsMargins(20, 0, 20, 0)
        self.loginContainerLayout:QLayout = QVBoxLayout(self.loginContainer)
        self.MAIN_LAYOUT.addWidget(self.loginContainer, alignment=Qt.AlignmentFlag.AlignCenter)

        self.emailField = QLineEdit()
        self.emailField.setStyleSheet(css.input_line_style())
        self.emailField.setPlaceholderText('Email')
        self.loginContainerLayout.addWidget(self.emailField)

        
        self.passwordField = QLineEdit()
        self.passwordField.setStyleSheet(css.input_line_style())
        self.passwordField.setPlaceholderText('Senha')
        self.passwordField.setEchoMode(QLineEdit.EchoMode.Password)
        self.loginContainerLayout.addWidget(self.passwordField)

        self.submitButton = QPushButton("Entrar")
        self.submitButton.setStyleSheet(css.simple_button())
        self.submitButton.setAttribute(Qt.WA_Hover, True)
        self.submitButton.setFixedSize(QSize(120, 40))
        self.loginContainerLayout.addWidget(self.submitButton, alignment=Qt.AlignmentFlag.AlignHCenter)