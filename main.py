from PySide6.QtWidgets import *
from ui.screens.main_window import MainWindow
from utils import *
import sys


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())