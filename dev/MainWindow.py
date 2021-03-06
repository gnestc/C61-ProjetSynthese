from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from dev.TakePicturesWindow import Ui_TakeTrainingPictures
from dev.PrepareDatasetWindow import Ui_PrepareDataset
from dev.DetectItemsWindow import Ui_DetectItems
from dev.MaskConfigWindow import Ui_MaskConfig

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        self.w1 = None
        self.w2 = None
        self.w3 = None
        self.maskWindow = None

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(13, 16, 13);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.onTakeTrainingPicturesClicked)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(430, 320, 220, 40))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
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
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(430, 380, 220, 40))
        self.pushButton_2.setFont(font)
        self.pushButton_2.clicked.connect(self.onDataPrepClicked)
        self.pushButton_2.setStyleSheet(u"QPushButton\n"
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
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(430, 440, 220, 40))
        self.pushButton_3.setFont(font)
        self.pushButton_3.clicked.connect(self.onDetectItemsClicked)
        self.pushButton_3.setStyleSheet(u"QPushButton\n"
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
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 60, 660, 221))
        self.label.setPixmap(QPixmap(u"./Crayorescent.png"))
        self.label.setScaledContents(True)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(410, 580, 261, 101))
        self.textEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                    "font: 8pt \"Consolas\";")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Sunken)
        self.textEdit.setLineWidth(1)
        self.textEdit.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1080, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Main Menu", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Take training pictures", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Prepare dataset", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Detect items", None))
        self.label.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:'Consolas'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">Submitted to Jean-Christophe Demers</span></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">by Carl Genest</span></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">in May 2021</span></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-l"
                                    "eft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">at C\u00e9gep du Vieux-Montr\u00e9al</span></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">as part of the<br />Projet Synth\u00e8se course </span></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">420-C61-IN</span></p></body></html>", None))
    # retranslateUi

    # Cr??ation de fen??tres dans PyQt/PySide:
    # https://www.learnpyqt.com/tutorials/creating-multiple-windows/
    def onTakeTrainingPicturesClicked(self, checked):
        if self.w1 is None:
            self.w1 = Ui_TakeTrainingPictures()
            self.w1.setupUi(self, self.w1)
            self.w1.run()
        else :
            self.w1.run()
            self.w1.comboBox.setCurrentIndex(0)
        self.w1.show()
        self.hide()

    def onDataPrepClicked(self):
        if self.w2 is None:
            self.w2 = Ui_PrepareDataset()
            self.w2.setupUi(self, self.w2)
        else:
            self.w2.photoList.clear()
        self.w2.show()
        self.hide()

    def onDetectItemsClicked(self):
        if self.w3 is None:
            self.w3 = Ui_DetectItems()
            self.w3.setupUi(self, self.w3)
            self.w3.run()
        else:
            self.w3.onDatasetListRefresh()
            self.w3.startTimer()
            self.w3.run()

        self.w3.show()
        self.hide()

    def onMaskClicked(self, color):
        if self.maskWindow is None:
            self.maskWindow = Ui_MaskConfig()
            self.maskWindow.setupUi(self, self.maskWindow)
            self.maskWindow.config(color)
            self.maskWindow.run()
        else:
            self.maskWindow.config(color)
            self.maskWindow.run()
        self.maskWindow.show()
        self.w2.hide()


