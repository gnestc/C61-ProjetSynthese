from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import cv2
import numpy as np
import qimage2ndarray
from datetime import datetime as dt
from dev.DAO import DAO


class Ui_PrepareDataset(QWidget):
    def setupUi(self, parent, Form):
        self.parent = parent
        self.entryList = None
        self.datasets = None
        self.colorValues = None

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

        self.photoList = QListWidget(Form)
        self.photoList.setObjectName(u"photoList")
        self.photoList.setGeometry(QRect(70, 360, 481, 161))
        self.photoList.clicked.connect(self.onListClicked)
        self.photoList.setStyleSheet(u"QListWidget\n"
                                      "{\n"
                                      "	background-color:rgb(30, 36, 30);\n"
                                      "	color: #FFF;\n"
                                      "}")

        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(180, 640, 841, 61))
        self.textBrowser.setStyleSheet(u"QTextBrowser\n"
                                       "{\n"
                                       "	color: #FFF;\n"
                                       "}")

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 30, 480, 270))
        self.label.setFrameShape(QFrame.StyledPanel)

        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(70, 310, 381, 31))
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

        self.create = QPushButton(Form)
        self.create.setObjectName(u"create")
        self.create.setGeometry(QRect(460, 310, 93, 40))
        self.create.setFont(font)
        self.create.clicked.connect(self.onCreateClicked)
        self.create.setStyleSheet(u"QPushButton\n"
                                  "{\n"
                                  "	border: 1px solid rgb(113, 203, 103);\n"
                                  "	border-radius: 20px;\n"
                                  "	color: #FFF;\n"
                                  "	padding-left: 20px;\n"
                                  "	padding-right: 20px;\n"
                                  "	background-color: rgb(30, 36, 30);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::hover\n"
                                  "{\n"
                                  "	background-color: rgb(63, 76, 63);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton::pressed\n"
                                  "{\n"
                                  "	background-color: rgb(113, 203, 103);\n"
                                  "}")

        self.colorValueList = QListWidget(Form)
        self.colorValueList.setObjectName(u"colorValueList")
        self.colorValueList.setGeometry(QRect(620, 30, 391, 271))
        self.colorValueList.setStyleSheet(u"QListWidget\n"
                                      "{\n"
                                      "	background-color:rgb(30, 36, 30);\n"
                                      "	color: #FFF;\n"
                                      "}")

        self.datasetList = QListWidget(Form)
        self.datasetList.setObjectName(u"datasetList")
        self.datasetList.setGeometry(QRect(620, 310, 391, 211))
        self.datasetList.clicked.connect(self.onDatasetListClicked)
        self.datasetList.setStyleSheet(u"QListWidget\n"
                                      "{\n"
                                      "	background-color:rgb(30, 36, 30);\n"
                                      "	color: #FFF;\n"
                                      "}")

        self.delete_btn = QPushButton(Form)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setGeometry(QRect(920, 530, 93, 40))
        self.delete_btn.setFont(font)
        self.delete_btn.clicked.connect(self.onDeleteClicked)
        self.delete_btn.setStyleSheet(u"QPushButton\n"
                                      "{\n"
                                      "	border: 1px solid rgb(113, 203, 103);\n"
                                      "	border-radius: 20px;\n"
                                      "	color: #FFF;\n"
                                      "	padding-left: 20px;\n"
                                      "	padding-right: 20px;\n"
                                      "	background-color: rgb(30, 36, 30);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::hover\n"
                                      "{\n"
                                      "	background-color: rgb(63, 76, 63);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::pressed\n"
                                      "{\n"
                                      "	background-color: rgb(113, 203, 103);\n"
                                      "}")

        self.mask_btn = QPushButton(Form)
        self.mask_btn.setObjectName(u"mask_btn")
        self.mask_btn.setGeometry(QRect(460, 530, 93, 40))
        self.mask_btn.setFont(font)
        self.mask_btn.clicked.connect(self.onMaskBtnClicked)
        self.mask_btn.setStyleSheet(u"QPushButton\n"
                                      "{\n"
                                      "	border: 1px solid rgb(113, 203, 103);\n"
                                      "	border-radius: 20px;\n"
                                      "	color: #FFF;\n"
                                      "	padding-left: 20px;\n"
                                      "	padding-right: 20px;\n"
                                      "	background-color: rgb(30, 36, 30);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::hover\n"
                                      "{\n"
                                      "	background-color: rgb(63, 76, 63);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::pressed\n"
                                      "{\n"
                                      "	background-color: rgb(113, 203, 103);\n"
                                      "}")

        self.onDatasetListRefresh()

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Prepare Dataset", None))
        self.back.setText(QCoreApplication.translate("Form", u"Back", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form",
                                                            u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select a color to verify the application of its mask or create a new dataset. The new dataset will contain the main color of every saved photo.\n"
                                                            "You can select the image on which you want to check the fit of the mask of the specified color. If the mask doesn't fit, take another picture with better lighting in previous step or change mask values.</p></body></html>",
                                                            None))
        #self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.create.setText(QCoreApplication.translate("Form", u"Create", None))
        self.delete_btn.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.mask_btn.setText(QCoreApplication.translate("Form", u"Masks", None))
    # retranslateUi


    def onBackClicked(self):
        self.comboBox.setCurrentIndex(0)
        self.textBrowser.setText("Select a color to verify the application of its mask or create a new dataset. The new dataset will contain the main color of every saved photo.\n"+
        "You can select the image on which you want to check the fit of the mask of the specified color. If the mask doesn't fit, take another picture with better lighting in previous step or change mask values.")
        self.close()
        self.parent.show()

    def onMaskBtnClicked(self):
        if self.comboBox.currentIndex() != 0:
            self.parent.onMaskClicked(self.comboBox.currentText())
        else:
            self.textBrowser.setText("Select a color to access its mask values")

    def on_combobox_changed(self):
        if self.comboBox.currentIndex() != 0:
            color=self.comboBox.currentText()
            self.photoListRefresh(color)

    def photoListRefresh(self, color):
        dao = DAO()
        self.entryList = dao.getImagesByColor(color)
        self.photoList.clear()
        if len(self.entryList) <= 15 and len(self.entryList) >= 2:
            for entry in self.entryList:
                self.photoList.addItem('{:12}'.format(entry[1])+entry[0])
            self.photoList.repaint()
            self.textBrowser.setText(str(len(self.entryList))+" "+color+" images were found. A minimum of 15 images is recommended.")
            self.selectedimageRefresh(-1)
        elif len(self.entryList) == 1:
            self.photoList.addItem('{:12}'.format(self.entryList[0][1]) + self.entryList[0][0])
            self.photoList.repaint()
            self.textBrowser.setText("Only "+str(len(self.entryList))+" "+color+" image was found. A minimum of 15 images is recommended.")
            self.selectedimageRefresh(-1)
        elif len(self.entryList) == 0:
            self.textBrowser.setText("No " + color + " photos were found")

    def onListClicked(self):
        row = self.photoList.currentRow()
        self.selectedimageRefresh(row)
        self.textBrowser.setText("Image with its color mask")

    def onDatasetListRefresh(self):
        dao = DAO()
        self.datasets = dao.getDatasetsByDate()
        self.datasetList.clear()
        if len(self.datasets) != 0:
            for dataset in self.datasets:
                self.datasetList.addItem('{:12}'.format("DS no."+str(dataset[0])) + dataset[1])
            self.datasetList.repaint()
            self.selectedDatasetRefresh(-1)

    def onDatasetListClicked(self):
        row = self.datasetList.currentRow()
        self.selectedDatasetRefresh(row)
        self.textBrowser.setText("Dataset content")

    def selectedDatasetRefresh(self, row):
        datasetNum = self.datasets[row][0]
        dao = DAO()
        self.colorValues = dao.getDatasetsContent(datasetNum)
        self.colorValueList.clear()

        for entry in self.colorValues:
            self.colorValueList.addItem('{:12}'.format(str(entry[0])) + str(entry[1]))

        self.colorValueList.repaint()

    def onDeleteClicked(self):
        row = self.datasetList.currentRow()
        datasetNum = self.datasets[row][0]
        dao = DAO()
        dao.deleteDataset(datasetNum)
        self.textBrowser.setText("Dataset deleted")
        self.onDatasetListRefresh()

    def getColorMaskValue(self, color):
        dao = DAO()
        mask = dao.getMask(color)

        lower = np.array(mask[0][1])
        upper = np.array(mask[0][2])

        return lower, upper

    def selectedimageRefresh(self, row):
        byteimg=self.entryList[row][2].tobytes()
        bufimg = np.frombuffer(byteimg, dtype=np.uint8)
        shapedimg = bufimg.reshape(360, 640, 3)
        hsv = cv2.cvtColor(shapedimg, cv2.COLOR_BGR2HSV)
        color = self.entryList[row][1]
        lower, upper = self.getColorMaskValue(color)

        maskcolor = cv2.inRange(hsv, lower, upper)
        image_res, image_thresh = cv2.threshold(maskcolor, 1, 255, cv2.THRESH_BINARY_INV)
        image_res, image_thresh_inv = cv2.threshold(image_thresh, 1, 255, cv2.THRESH_BINARY_INV)
        shapedimg = cv2.bitwise_and(shapedimg, shapedimg, mask=image_thresh_inv)

        cvtimg = cv2.cvtColor(shapedimg, cv2.COLOR_BGR2RGB)
        qimg = qimage2ndarray.array2qimage(cvtimg)
        self.label.setPixmap(QPixmap.fromImage(qimg))

    def onCreateClicked(self):
        dao = DAO()
        entryList = dao.getTrainingImages()
        centers=[["No object", [0, 0, 0]]]
        for entry in entryList:
            byteimg = entry[2].tobytes()
            bufimg = np.frombuffer(byteimg, dtype=np.uint8)
            shapedimg = bufimg.reshape(360, 640, 3)
            hsv = cv2.cvtColor(shapedimg, cv2.COLOR_BGR2HSV)
            color = entry[1]
            lower, upper = self.getColorMaskValue(color)

            maskcolor = cv2.inRange(hsv, lower, upper)
            image_res, image_thresh = cv2.threshold(maskcolor, 1, 255, cv2.THRESH_BINARY_INV)
            image_res, image_thresh_inv = cv2.threshold(image_thresh, 1, 255, cv2.THRESH_BINARY_INV)
            img = cv2.bitwise_and(shapedimg, shapedimg, mask=image_thresh_inv)

            # Référence - Exemple de code du K-Means tel que fourni par OpenCV :
            # https://docs.opencv.org/master/d1/d5c/tutorial_py_kmeans_opencv.html

            Z = img.reshape((-1, 3))
            Z = np.float32(Z)

            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
            k = 2

            attempts = 20
            ret, label, center = cv2.kmeans(Z, k, None, criteria, attempts, cv2.KMEANS_PP_CENTERS)

            center = np.uint8(center)
            center = center.tolist()
            if center[1][0] != 0 and center[1][1] != 0 and center[1][2] != 0 :
                center = [color, center[1]]
            else:
                center = [color, center[0]]
            centers.append(center)

        date = dt.now()
        dateString = "Created on " + str(date.year) + "/" + str(date.month) + "/" + str(date.day) + " at " + str(date.hour) + ":" + str(date.minute) + ":" + str(date.second) + ":" + str(date.microsecond % 10)
        dao = DAO()
        dao.insertDataset(centers, dateString)
        self.textBrowser.setText("Color values from "+str(len(centers)-1)+ " photos were successfully saved.")
        self.onDatasetListRefresh()