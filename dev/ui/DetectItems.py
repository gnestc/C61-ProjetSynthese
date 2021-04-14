from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import cv2
import numpy as np
import qimage2ndarray
from datetime import datetime as dt
from dev.DAO import DAO

class Ui_DetectItems(QWidget):
    def setupUi(self, parent, Form):
        self.parent = parent

        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1080, 720)
        Form.setStyleSheet(u"background-color: rgb(13, 16, 13);")

        self.back = QPushButton(Form)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(70, 640, 93, 40))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(7)
        self.back.setFont(font)
        self.back.clicked.connect(self.onBackClicked)
        self.back.setStyleSheet(u"QPushButton\n"
                                "{\n"
                                "	border: 1px solid rgb(113, 203, 103);\n"
                                "	border-radius: 20px;\n"
                                "	color: #FFF;\n"
                                "	padding-left: 20px;\n"
                                "	padding-right: 20px;\n"
                                "	background-color: rgb(30, 36, 30)\n"
                                "}\n"
                                "\n"
                                "QPushButton::hover\n"
                                "{\n"
                                "	background-color: rgb(63, 76, 63);\n"
                                "\n"
                                "}\n"
                                "\n"
                                "QPushButton::pressed\n"
                                "{\n"
                                "	background-color: rgb(113, 203, 103);\n"
                                "\n"
                                "}")
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Detect items", None))
        self.back.setText(QCoreApplication.translate("Form", u"Back", None))

    # retranslateUi

    def onBackClicked(self):
        #self.textBrowser.setText("Select a color to verify the application of its mask or create a new dataset. The new dataset will contain the main color of every saved photo.\n"+
        #"You can select the image on which you want to check the fit of the mask of the specified color. If the mask doesn't fit, take another picture with better lighting in previous step or change mask values.")
        self.close()
        self.parent.show()

    def closeEvent(self, event) :
        #self.timer.stop()
        #self.cap.release()
        self.parent.close()