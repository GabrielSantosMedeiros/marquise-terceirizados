from PySide6.QtWidgets import *
from ui import css
from controller import ScreenController
from utils import *


@singleton
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setStyleSheet(css.background_style())

        stack:QWidget = ScreenController().getStack()

        self.setCentralWidget(stack)
