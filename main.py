from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui import css
from ui.login_screen import LoginScreen
from utils import *
from typing import *
import sys


@singleton
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setStyleSheet(css.background_style)

        stack:QWidget = QStackedWidget()
        stack.addWidget(LoginScreen())

        self.setCentralWidget(stack)




if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())