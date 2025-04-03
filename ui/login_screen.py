from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from utils import *
from typing import *

@singleton
class LoginScreen(QWidget):

    def __init__(self):
        super().__init__()

        loginContainer:QWidget = QFrame()