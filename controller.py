from PySide6.QtCore import Signal
from PySide6.QtWidgets import QStackedWidget, QFrame
from ui.screens.login_screen import LoginScreen
from ui.screens.home_screen import HomeScreen
from utils import *

@singleton
class ScreenController:

    def __init__(self):

        self.stack = QStackedWidget()

        self.login_screen = LoginScreen()
        self.login_screen.LOGIN_VALID.connect(self.switchScreen)
        self.stack.addWidget(self.login_screen)

        self.home_screen = HomeScreen()
        self.stack.addWidget(self.home_screen)
        
        self.stack.setCurrentWidget(self.home_screen)
    

    def getStack(self): 
        return self.stack


    def switchScreen(self):
        self.stack.setCurrentWidget(self.home_screen)