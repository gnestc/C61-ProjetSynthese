import os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import cv2
import qimage2ndarray
from datetime import datetime as dt


class Ui_TakeTrainingPictures(QWidget):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1080, 720)
        Form.setStyleSheet(u"background-color: rgb(13, 16, 13);")
        self.frame = None
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 400, 201, 40))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(7)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.onBackClicked)
        self.pushButton.setStyleSheet(u"QPushButton\n"
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
        self.pushButton2 = QPushButton(Form)
        self.pushButton2.setObjectName(u"pushButton")
        self.pushButton2.setGeometry(QRect(40, 400, 201, 40))
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet(u"QPushButton\n"
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
        self.pushButton2.clicked.connect(self.take)

        self.labelPic = QLabel(Form)
        self.labelPic.setObjectName(u"labelPic")
        self.labelPic.setGeometry(QRect(10, 40, 640, 360))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Back", None))
        self.pushButton2.setText(QCoreApplication.translate("Form", u"Take", None))
        #self.labelPic.setText(QCoreApplication.translate("Form", u"labelPic", None))
    # retranslateUi

    def displayFrame(self):
        ret, self.frame = self.cap.read()
        #fgmask = self.fgbg.apply(self.frame)
        #self.frame = cv2.bitwise_and(self.frame, self.frame, mask=fgmask)
        self.frame2 = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.image = qimage2ndarray.array2qimage(self.frame2)
        self.labelPic.setPixmap(QPixmap.fromImage(self.image))

    def run(self):
        self.cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        #self.fgbg = cv2.createBackgroundSubtractorMOG2()
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
        self.timer = QTimer()
        self.timer.timeout.connect(self.displayFrame)
        self.timer.start(60)

    def closeEvent(self, event) :
        self.timer.stop()
        self.cap.release()

    def onBackClicked(self):
        self.close()

    def take(self):
        if self.frame.any() != None:
            print("Image saved")
            date = dt.now()
            img_name = "crayorescent_"+str(date.year)+str(date.month)+str(date.day)+"_"+str(date.hour)+str(date.minute)+str(date.second)+str(date.microsecond%10)+".jpg"
            path = "C:/Users/gnest/Documents/GitHub/C61-ProjetSynthese/dev/img/"
            cv2.imwrite(os.path.join(path, img_name), self.frame)
