from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import cv2
import qimage2ndarray
from dev.DAO import DAO
from dev.ColorRecognition import ColorRecognition
import math

class Ui_DetectItems(QWidget):
    def setupUi(self, parent, Form):
        self.parent = parent
        self.frame = None
        self.datasets = None

        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1080, 720)
        Form.setStyleSheet(u"background-color: rgb(13, 16, 13);")

        self.back = QPushButton(Form)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(80, 600, 91, 40))
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

        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(80, 410, 481, 171))
        self.textBrowser.setStyleSheet(u"QTextBrowser\n"
                                       "{\n"
                                       "	color: #FFF;\n"
                                       "}")

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 70, 480, 270))
        self.label.setFrameShape(QFrame.StyledPanel)

        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(670, 410, 331, 171))
        self.listWidget.setStyleSheet(u"QListWidget\n"
                                      "{\n"
                                      "	background-color:rgb(30, 36, 30);\n"
                                      "	color: #FFF;\n"
                                      "}")

        self.select = QPushButton(Form)
        self.select.setObjectName(u"select")
        self.select.setGeometry(QRect(670, 600, 91, 40))
        self.select.setStyleSheet(u"QPushButton\n"
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
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(670, 70, 331, 271))
        self.label_2.setFrameShape(QFrame.StyledPanel)

        self.onDatasetListRefresh()

        self.timerDetect = QTimer()
        self.timerDetect.timeout.connect(self.detect)
        self.timerDetect.start(2000)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Detect items", None))
        self.back.setText(QCoreApplication.translate("Form", u"Back", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.select.setText(QCoreApplication.translate("Form", u"Select", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form",
                                                            u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Place an object in front of the camera on a white background and the corresponding color will be detected. Change dataset as needed.</p></body></html>",
                                                            None))
    # retranslateUi

    def detect(self):
        colorDetect = ColorRecognition()
        center=colorDetect.run(self.frame)
        if center[0]==0 and center[1]==0 and center[2]==0:
            self.textBrowser.setText("No object detected")
        else:
            datasetNum = self.datasets[self.listWidget.currentRow()][0]
            dao = DAO()
            self.colorValues = dao.getDatasetsContent(datasetNum)
            self.knn(center, self.colorValues)

    def knn(self, center, colorValues):
        #print(center, colorValues)

        distances=[]
        for pt in colorValues :
            res=math.sqrt(math.pow(center[0]-pt[1][0], 2)+math.pow(center[1]-pt[1][1], 2) + math.pow(center[2]-pt[1][2], 2))
            distances.append(res)
        lowest=min(distances)
        index=distances.index(lowest)
        self.textBrowser.setText(str(colorValues[index][0]))

    def displayFrame(self):
        ret, self.frame = self.cap.read()
        self.frame2 = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.image = qimage2ndarray.array2qimage(self.frame2)
        self.label.setPixmap(QPixmap.fromImage(self.image))

    def run(self):
        self.cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        if self.cap is None or not self.cap.isOpened():
            self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

        self.timer = QTimer()
        self.timer.timeout.connect(self.displayFrame)
        self.timer.start(60)

    def onDatasetListRefresh(self):
        dao = DAO()
        self.datasets = dao.getDatasetsByDate()
        self.listWidget.clear()
        if len(self.datasets) != 0:
            for dataset in self.datasets:
                self.listWidget.addItem('{:12}'.format("DS no."+str(dataset[0])) + dataset[1])
            self.listWidget.repaint()

    def onBackClicked(self):
        #self.textBrowser.setText("Select a color to verify the application of its mask or create a new dataset. The new dataset will contain the main color of every saved photo.\n"+
        #"You can select the image on which you want to check the fit of the mask of the specified color. If the mask doesn't fit, take another picture with better lighting in previous step or change mask values.")
        self.onDatasetListRefresh()
        self.close()
        self.timer.stop()
        self.timerDetect.stop()
        self.cap.release()
        self.parent.show()

    def closeEvent(self, event) :
        #self.timer.stop()
        #self.cap.release()
        self.timer.stop()
        self.timerDetect.stop()
        self.cap.release()
        self.parent.close()