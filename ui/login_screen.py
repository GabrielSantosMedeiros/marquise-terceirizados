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

        loginContainer:QWidget = QFrame()
        loginContainer.setStyleSheet(css.wireframe_style)
        loginContainer.setFixedSize(QSize(683, 384))
        
        self.MAIN_LAYOUT.addWidget(loginContainer, alignment=Qt.AlignmentFlag.AlignCenter)