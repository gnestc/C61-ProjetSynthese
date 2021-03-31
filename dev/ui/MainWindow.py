from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import dev.TakingPictures as tp
from dev.ui.TakePicturesWindow import Ui_TakeTrainingPictures
#import dev.TakingPictures as take

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        self.w = None
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
        self.label.setPixmap(QPixmap(u"./ui/Crayorescent.png"))
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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

    def onTakeTrainingPicturesClicked(self, checked):
        if self.w is None:
            self.w = Ui_TakeTrainingPictures()
            self.w.setupUi(self.w)
            self.w.run()
        else :
            self.w.run()
        self.w.show()


