from PySide2.QtWidgets import *

import sys
from dev.MainWindow import Ui_MainWindow

class Main:
    def __init__(self):
        self.execute()

    def execute(self):
        self.app = QApplication(sys.argv)
        self.window = Ui_MainWindow()
        self.window.setupUi(self.window)
        self.window.show()
        self.app.exec_()

def main():
    m = Main()

if __name__ == '__main__':
    quit(main())

