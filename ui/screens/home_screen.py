from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui import css


class HomeScreen(QWidget):

    def __init__(self):
        super().__init__()

        self.mainContainer = QHBoxLayout(self)
        
        self.menuContainter = QFrame()
        self.menuLayout = QVBoxLayout(self.menuContainter)

        
        self.dashboardButton = QPushButton("Dashboard")
        self.dashboardButton.setStyleSheet(css.simple_button())
        self.menuLayout.addWidget(self.dashboardButton)

        self.empresasButton = QPushButton("Empresas")
        self.empresasButton.setStyleSheet(css.simple_button())
        self.menuLayout.addWidget(self.empresasButton)

        self.veiculosButton = QPushButton("Veiculos")
        self.veiculosButton.setStyleSheet(css.simple_button())
        self.menuLayout.addWidget(self.veiculosButton)


        self.funcionariosButton = QPushButton("Funcionarios")
        self.funcionariosButton.setStyleSheet(css.simple_button())
        self.menuLayout.addWidget(self.funcionariosButton)

        





        self.contentContainer = QFrame()
        self.contentLayout = QVBoxLayout(self.contentContainer)



        self.mainContainer.addWidget(self.menuContainter)


        