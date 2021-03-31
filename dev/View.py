from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import sys
from ui.MainWindow import Ui_MainWindow

class View:
    def __init__(self, parent):
        self.parent = parent
        self.execute()

    def execute(self):
        self.app = QApplication(sys.argv)
        self.window = Ui_MainWindow()
        self.window.setupUi(self.window)
        self.window.show()
        self.app.exec_()

