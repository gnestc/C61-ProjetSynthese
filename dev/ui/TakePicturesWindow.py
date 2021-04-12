import binascii
import os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import cv2
import numpy as np
from PIL import Image
import io
import qimage2ndarray
from datetime import datetime as dt
from dev.DAO import DAO


class Ui_TakeTrainingPictures(QWidget):
    def setupUi(self, parent, Form):
        self.parent = parent
        self.entryList = None
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1080, 720)
        Form.setStyleSheet(u"background-color: rgb(13, 16, 13);")
        self.frame = None
        self.back = QPushButton(Form)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(40, 640, 91, 40))
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
        self.takebtn = QPushButton(Form)
        self.takebtn.setObjectName(u"takebtn")
        self.takebtn.setGeometry(QRect(40, 380, 91, 40))
        self.takebtn.setFont(font)
        self.takebtn.setStyleSheet(u"QPushButton\n"
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
        self.takebtn.clicked.connect(self.takeInDB)

        self.livecam = QLabel(Form)
        self.livecam.setObjectName(u"livecam")
        self.livecam.setGeometry(QRect(40, 70, 480, 270))
        self.livecam.setStyleSheet(u"QLabel{\n"
                                   "	background-color:rgb(30, 36, 30)\n"
                                   "}")
        self.livecam.setFrameShape(QFrame.NoFrame)
        self.livecam.setFrameShadow(QFrame.Plain)
        self.livecam.setLineWidth(1)

        self.photoList = QListWidget(Form)
        self.photoList.setObjectName(u"photoList")
        self.photoList.setGeometry(QRect(560, 380, 480, 171))
        self.photoList.setStyleSheet(u"QListWidget{\n"
                                    "	background-color: rgb(30, 36, 30);\n"
                                    "	color: #FFF;\n"
                                    "}")
        self.photoList.setFrameShape(QFrame.NoFrame)
        self.photoList.clicked.connect(self.onListClicked)

        self.selectedimage = QLabel(Form)
        self.selectedimage.setObjectName(u"selectedimage")
        self.selectedimage.setGeometry(QRect(560, 70, 480, 270))
        self.selectedimage.setStyleSheet(u"QLabel{\n"
                                         "	background-color: rgb(30, 36, 30)\n"
                                         "}")

        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(140, 384, 380, 31))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
                                    "	background-color: rgb(30, 36, 30);\n"
                                    "	color: #FFF;\n"
                                    "}"
                                    "QListView"
                                    "{"
                                    "background-color: rgb(30, 36, 30);"
                                    "color: #FFF;"
                                    "}")
        combolist = ["Select a color","Red", "Pink", "Orange", "Yellow", "Green", "Blue"]
        self.comboBox.addItems(combolist)
        self.comboBox.currentTextChanged.connect(self.on_combobox_changed)

        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(40, 440, 480, 71))
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(u"QTextBrowser{\n"
                                       "	color: #FFF;\n"
                                       "}")
        self.textBrowser.setText("Select a color, place the object in front of the camera on a white surface and take a photo.")

        self.delete_btn = QPushButton(Form)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setGeometry(QRect(950, 570, 91, 40))
        self.delete_btn.setFont(font)
        self.delete_btn.clicked.connect(self.onDeleteClicked)
        self.delete_btn.setStyleSheet(u"QPushButton\n"
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

        self.photoListRefresh()
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Take Training Pictures", None))
        self.back.setText(QCoreApplication.translate("Form", u"Back", None))
        self.takebtn.setText(QCoreApplication.translate("Form", u"Take", None))
        #self.selectedimage.setText("")
        #self.comboBox.setPlaceholderText(QCoreApplication.translate("Form", u"Select a color", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form",
                                                            u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "</style></head><body style=\" font-family:'Consolas'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
                                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select the color that matches the object, place the object in front of the camera on a white surface and take a photo.</p></body></html>",
                                                            None))
        self.delete_btn.setText(QCoreApplication.translate("Form", u"Delete", None))
    # retranslateUi

    def on_combobox_changed(self):
        if self.comboBox.currentIndex() != 0:
            self.textBrowser.setText("Ready for a take\n\nThe photo will then be saved automatically with its associated color")
        else:
            self.textBrowser.setText("Select the color that matches the object, place the object in front of the camera on a white surface and take a photo.")

    def displayFrame(self):
        ret, self.frame = self.cap.read()
        #fgmask = self.fgbg.apply(self.frame)
        #self.frame = cv2.bitwise_and(self.frame, self.frame, mask=fgmask)
        self.frame2 = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.image = qimage2ndarray.array2qimage(self.frame2)
        self.livecam.setPixmap(QPixmap.fromImage(self.image))

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
        self.textBrowser.setText("Select the color that matches the object, place the object in front of the camera on a white surface and take a photo.")
        self.close()
        self.parent.show()

    def closeEvent(self, event):
        self.parent.close()

    def take(self):
        if self.frame.any() != None:
            date = dt.now()
            img_name = "crayorescent_"+str(date.year)+str(date.month)+str(date.day)+"_"+str(date.hour)+str(date.minute)+str(date.second)+str(date.microsecond%10)+".jpg"
            path = "C:/Users/gnest/Documents/GitHub/C61-ProjetSynthese/dev/img/"
            cv2.imwrite(os.path.join(path, img_name), self.frame)
            print("Image saved")

    def takeInDB(self):
        if self.frame.any() != None and self.comboBox.currentIndex() != 0:
            dao = DAO()
            colorName=self.comboBox.currentText()
            date = dt.now()
            dateString = "Taken on " + str(date.year) + "/" + str(date.month) + "/" + str(date.day) + " at " + str(date.hour) + ":" + str(date.minute) + ":" + str(date.second) + ":" + str(date.microsecond % 10)
            dao.insertDB(dateString, colorName, self.frame)
            self.photoListRefresh()
            self.textBrowser.setText("Image saved\n\nReady for the next take")

        elif self.comboBox.currentIndex() == 0:
            self.textBrowser.setText("Error: object color not selected")

    def photoListRefresh(self):
        dao = DAO()
        self.entryList = dao.getTrainingImages()
        self.photoList.clear()
        if len(self.entryList) != 0:
            for entry in self.entryList:
                self.photoList.addItem('{:12}'.format(entry[1])+entry[0])
            self.photoList.repaint()

            self.selectedimageResfresh(-1)

    def onListClicked(self):
        row = self.photoList.currentRow()
        self.selectedimageResfresh(row)
        self.textBrowser.setText("Image as saved in the database")

    def selectedimageResfresh(self, row):
        byteimg=self.entryList[row][2].tobytes()
        bufimg = np.frombuffer(byteimg, dtype=np.uint8)
        bufimg = bufimg.reshape(360, 640, 3)
        cvtimg = cv2.cvtColor(bufimg, cv2.COLOR_BGR2RGB)
        qimg = qimage2ndarray.array2qimage(cvtimg)
        self.selectedimage.setPixmap(QPixmap.fromImage(qimg))

    def onDeleteClicked(self):
        if self.textBrowser.toPlainText() == "Image as saved in the database":
            row = self.photoList.currentRow()
            key = self.entryList[row][0]
            dao = DAO()
            dao.deleteImg(key)
            self.photoListRefresh()
            self.textBrowser.setText("Image deleted")
        else :
            self.textBrowser.setText("Select an image from the list before deleting")