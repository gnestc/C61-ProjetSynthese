# Référence - Ajustement des masques :
# https://www.youtube.com/watch?v=Tj4zEX_pdUg
import qimage2ndarray
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import numpy as np
import cv2
from dev.DAO import DAO

class Ui_MaskConfig(QWidget):
    def setupUi(self, parent, Form):
        self.color = None
        self.parent=parent
        self.frame = None
        self.hueMinValue = None
        self.hueMaxValue = None
        self.satMinValue = None
        self.satMaxValue = None
        self.valMinValue = None
        self.valMaxValue = None

        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1080, 720)
        Form.setStyleSheet(u"background-color: rgb(13, 16, 13);")

        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(7)

        self.back = QPushButton(Form)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(40, 640, 91, 40))
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

        self.viewBlack = QLabel(Form)
        self.viewBlack.setObjectName(u"viewBlack")
        self.viewBlack.setGeometry(QRect(70, 30, 480, 270))
        self.viewBlack.setStyleSheet(u"QLabel{\n"
                                     "	background-color: rgb(30, 36, 30)\n"
                                     "}")

        self.hueMinBar = QSlider(Form)
        self.hueMinBar.setObjectName(u"hueMinBar")
        self.hueMinBar.setGeometry(QRect(119, 340, 381, 21))
        self.hueMinBar.setOrientation(Qt.Horizontal)
        self.hueMinBar.setMinimum(0)
        self.hueMinBar.setMaximum(179)
        self.hueMinBar.valueChanged.connect(self.hueMinMoved)
        self.hueMinBar.setStyleSheet("color: #FFF;")

        self.hueMaxBar = QSlider(Form)
        self.hueMaxBar.setObjectName(u"hueMaxBar")
        self.hueMaxBar.setGeometry(QRect(120, 380, 381, 21))
        self.hueMaxBar.setOrientation(Qt.Horizontal)
        self.hueMaxBar.setMinimum(0)
        self.hueMaxBar.setMaximum(179)
        self.hueMaxBar.valueChanged.connect(self.hueMaxMoved)
        self.hueMaxBar.setStyleSheet("color: #FFF;")

        self.satMinBar = QSlider(Form)
        self.satMinBar.setObjectName(u"satMinBar")
        self.satMinBar.setGeometry(QRect(120, 440, 381, 21))
        self.satMinBar.setOrientation(Qt.Horizontal)
        self.satMinBar.setMinimum(0)
        self.satMinBar.setMaximum(255)
        self.satMinBar.valueChanged.connect(self.satMinMoved)
        self.satMinBar.setStyleSheet("color: #FFF;")

        self.satMaxBar = QSlider(Form)
        self.satMaxBar.setObjectName(u"satMaxBar")
        self.satMaxBar.setGeometry(QRect(120, 480, 381, 21))
        self.satMaxBar.setOrientation(Qt.Horizontal)
        self.satMaxBar.setMinimum(0)
        self.satMaxBar.setMaximum(255)
        self.satMaxBar.valueChanged.connect(self.satMaxMoved)
        self.satMaxBar.setStyleSheet("color: #FFF;")

        self.valMinBar = QSlider(Form)
        self.valMinBar.setObjectName(u"valMinBar")
        self.valMinBar.setGeometry(QRect(120, 540, 381, 21))
        self.valMinBar.setOrientation(Qt.Horizontal)
        self.valMinBar.setMinimum(0)
        self.valMinBar.setMaximum(255)
        self.valMinBar.valueChanged.connect(self.valMinMoved)
        self.valMinBar.setStyleSheet("color: #FFF;")

        self.valMaxBar = QSlider(Form)
        self.valMaxBar.setObjectName(u"valMaxBar")
        self.valMaxBar.setGeometry(QRect(120, 580, 381, 21))
        self.valMaxBar.setOrientation(Qt.Horizontal)
        self.valMinBar.setMinimum(0)
        self.valMaxBar.setMaximum(255)
        self.valMaxBar.valueChanged.connect(self.valMaxMoved)
        self.valMaxBar.setStyleSheet("color: #FFF;")


        self.viewBW = QLabel(Form)
        self.viewBW.setObjectName(u"viewBW")
        self.viewBW.setGeometry(QRect(590, 30, 480, 270))
        self.viewBW.setStyleSheet(u"QLabel{\n"
                                  "	background-color: rgb(30, 36, 30)\n"
                                  "}")

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(14, 340, 91, 20))
        self.label_3.setStyleSheet(u"color: #FFF;")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(14, 380, 91, 20))
        self.label_4.setStyleSheet(u"color: #FFF;")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(14, 440, 91, 20))
        self.label_5.setStyleSheet(u"color: #FFF;")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(14, 480, 91, 20))
        self.label_6.setStyleSheet(u"color: #FFF;")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(14, 540, 91, 20))
        self.label_7.setStyleSheet(u"color: #FFF;")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(14, 580, 91, 20))
        self.label_8.setStyleSheet(u"color: #FFF;")

        self.resMinHue = QLabel(Form)
        self.resMinHue.setObjectName(u"resMinHue")
        self.resMinHue.setGeometry(QRect(520, 340, 55, 21))
        self.resMinHue.setStyleSheet(u"color: #FFF;")
        self.resMinHue.setFrameShape(QFrame.StyledPanel)
        self.resMaxHue = QLabel(Form)
        self.resMaxHue.setObjectName(u"resMaxHue")
        self.resMaxHue.setGeometry(QRect(520, 380, 55, 21))
        self.resMaxHue.setStyleSheet(u"color: #FFF;")
        self.resMaxHue.setFrameShape(QFrame.StyledPanel)
        self.resMinSat = QLabel(Form)
        self.resMinSat.setObjectName(u"resMinSat")
        self.resMinSat.setGeometry(QRect(520, 440, 55, 21))
        self.resMinSat.setStyleSheet(u"color: #FFF;")
        self.resMinSat.setFrameShape(QFrame.StyledPanel)
        self.resMaxSat = QLabel(Form)
        self.resMaxSat.setObjectName(u"resMaxSat")
        self.resMaxSat.setGeometry(QRect(520, 480, 55, 21))
        self.resMaxSat.setStyleSheet(u"color: #FFF;")
        self.resMaxSat.setFrameShape(QFrame.StyledPanel)
        self.resMinVal = QLabel(Form)
        self.resMinVal.setObjectName(u"resMinVal")
        self.resMinVal.setGeometry(QRect(520, 540, 55, 21))
        self.resMinVal.setStyleSheet(u"color: #FFF;")
        self.resMinVal.setFrameShape(QFrame.StyledPanel)
        self.resMaxVal = QLabel(Form)
        self.resMaxVal.setObjectName(u"resMaxVal")
        self.resMaxVal.setGeometry(QRect(520, 580, 55, 21))
        self.resMaxVal.setStyleSheet(u"color: #FFF;")
        self.resMaxVal.setFrameShape(QFrame.StyledPanel)

        self.viewOriginal = QLabel(Form)
        self.viewOriginal.setObjectName(u"viewOriginal")
        self.viewOriginal.setGeometry(QRect(590, 330, 480, 270))
        self.viewOriginal.setStyleSheet(u"QLabel{\n"
                                        "	background-color: rgb(30, 36, 30)\n"
                                        "}")
        self.save = QPushButton(Form)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(160, 640, 91, 40))
        self.save.clicked.connect(self.onSaveClicked)
        self.save.setStyleSheet(u"QPushButton\n"
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

        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(300, 640, 480, 71))
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(u"QTextBrowser{\n"
                                       "	color: #FFF;\n"
                                       "}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.back.setText(QCoreApplication.translate("Form", u"Back", None))
        self.viewBlack.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.viewBW.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Min hue", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Max hue", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Min saturation", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Max saturation", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Min value", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Max value", None))
        self.resMinHue.setText("")
        self.resMaxHue.setText("")
        self.resMinSat.setText("")
        self.resMaxSat.setText("")
        self.resMinVal.setText("")
        self.resMaxVal.setText("")
        self.viewOriginal.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.save.setText(QCoreApplication.translate("Form", u"Save", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form",
                                                            u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "</style></head><body style=\" font-family:'Consolas'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
                                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Put an object of the selected color on a white surface in front of the camera. Drag each of the sliders until the color is isolated and save your changes.</p></body></html>",
                                                            None))

    # retranslateUi
    def displayFrame(self):
        ret, self.frame = self.cap.read()
        self.frame2 = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.image = qimage2ndarray.array2qimage(self.frame2)
        self.viewOriginal.setPixmap(QPixmap.fromImage(self.image))

        imghsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

        lower = np.array([self.hueMinValue, self.satMinValue, self.valMinValue])
        upper = np.array([self.hueMaxValue, self.satMaxValue, self.valMaxValue])

        mask = cv2.inRange(imghsv, lower, upper)
        res = cv2.bitwise_and(self.frame2, self.frame2, mask=mask)

        mask2 = qimage2ndarray.array2qimage(mask)
        res2 = qimage2ndarray.array2qimage(res)

        self.viewBW.setPixmap(QPixmap.fromImage(mask2))
        self.viewBlack.setPixmap(QPixmap.fromImage(res2))

    def run(self):
        self.cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        if self.cap is None or not self.cap.isOpened():
            self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

        self.timer = QTimer()
        self.timer.timeout.connect(self.displayFrame)
        self.timer.start(60)

    def config(self, color):
        self.color=color
        dao = DAO()
        mask = dao.getMask(color)

        self.hueMinBar.setValue(mask[0][1][0])
        self.hueMinValue = mask[0][1][0]
        self.resMinHue.setText(str(mask[0][1][0]))
        self.hueMaxBar.setValue(mask[0][2][0])
        self.hueMaxValue = mask[0][2][0]
        self.resMaxHue.setText(str(mask[0][2][0]))
        self.satMinBar.setValue(mask[0][1][1])
        self.satMinValue = mask[0][1][1]
        self.resMinSat.setText(str(mask[0][1][1]))
        self.satMaxBar.setValue(mask[0][2][1])
        self.satMaxValue = mask[0][2][1]
        self.resMaxSat.setText(str(mask[0][2][1]))
        self.valMinBar.setValue(mask[0][1][2])
        self.valMinValue = mask[0][1][2]
        self.resMinVal.setText(str(mask[0][1][2]))
        self.valMaxBar.setValue(mask[0][2][2])
        self.valMaxValue = mask[0][2][2]
        self.resMaxVal.setText(str(mask[0][2][2]))

    def onSaveClicked(self):

        savedValues=[self.color, [self.hueMinValue, self.satMinValue, self.valMinValue], [self.hueMaxValue, self.satMaxValue, self.valMaxValue]]
        dao=DAO()
        dao.updateMask(savedValues)
        self.textBrowser.setText("Saved successfully")
        self.config(self.color)

    def onBackClicked(self):
        self.close()
        self.timer.stop()
        self.cap.release()
        self.parent.w2.selectedimageRefresh(-1)
        self.parent.w2.show()
        self.textBrowser.setText("Put an object of the selected color on a white surface in front of the camera. Drag each of the sliders until the color is isolated and save your changes.")

    def closeEvent(self, event) :
        self.timer.stop()
        self.cap.release()
        self.parent.w2.show()


    def hueMinMoved(self):
        self.hueMinValue=self.hueMinBar.value()
        self.resMinHue.setText(str(self.hueMinValue))

    def hueMaxMoved(self):
        self.hueMaxValue=self.hueMaxBar.value()
        self.resMaxHue.setText(str(self.hueMaxValue))

    def satMinMoved(self):
        self.satMinValue=self.satMinBar.value()
        self.resMinSat.setText(str(self.satMinValue))

    def satMaxMoved(self):
        self.satMaxValue=self.satMaxBar.value()
        self.resMaxSat.setText(str(self.satMaxValue))

    def valMinMoved(self):
        self.valMinValue=self.valMinBar.value()
        self.resMinVal.setText(str(self.valMinValue))

    def valMaxMoved(self):
        self.valMaxValue=self.valMaxBar.value()
        self.resMaxVal.setText(str(self.valMaxValue))
