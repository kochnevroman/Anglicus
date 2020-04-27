# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fourth_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

class Ui_View_4(object):
    def setupUi(self, View_4):
        View_4.setObjectName("Fourth View")
        View_4.resize(715, 570)
        self.centralwidget = QtWidgets.QWidget(View_4)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #fff")

        self.Palet = QtWidgets.QLabel(self.centralwidget)
        self.Palet.setGeometry(QtCore.QRect(20, 20, 341, 500))
        self.Palet.setText("")
        self.Palet.setObjectName("Palet")
        self.Palet.setStyleSheet('''
                                                     background-color: #F6ED9A;
                                                     border-color: #F6ED9A;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                     ''')

        self.TestsLabel = QtWidgets.QLabel(self.centralwidget)
        self.TestsLabel.setGeometry(QtCore.QRect(156, 40, 71, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(26)
        self.TestsLabel.setFont(font)
        self.TestsLabel.setObjectName("TestsLabel")
        self.TestsLabel.setStyleSheet("background-color: #F6ED9A")

        self.NackNarrowImage = QtWidgets.QLabel(self.centralwidget)
        self.NackNarrowImage.setGeometry(QtCore.QRect(30, 40, 41, 41))
        self.NackNarrowImage.setText("")
        self.NackNarrowImage.setObjectName("NackNarrowImage")
        self.NackNarrowImage.setStyleSheet("background-color: #F6ED9A")

        self.DescriptionTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.DescriptionTextBrowser.setGeometry(QtCore.QRect(420, 140, 256, 181))
        self.DescriptionTextBrowser.setObjectName("DescriptionTextBrowser")
        self.DescriptionTextBrowser.setStyleSheet('''
                                                                    background-color: #fff;
                                                                    border: none;
                                                                    ''')

        self.Test_1Button = QtWidgets.QPushButton(self.centralwidget)
        self.Test_1Button.setGeometry(QtCore.QRect(40, 130, 300, 51))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(22)
        self.Test_1Button.setFont(font)
        self.Test_1Button.setObjectName("Test_1Button")
        self.Test_1Button.setStyleSheet("background-color: #F6ED9A")

        self.Test_2Button = QtWidgets.QPushButton(self.centralwidget)
        self.Test_2Button.setGeometry(QtCore.QRect(40, 210, 300, 51))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(22)
        self.Test_2Button.setFont(font)
        self.Test_2Button.setObjectName("Test_2Button")
        self.Test_2Button.setStyleSheet("background-color: #F6ED9A")

        self.Test_3Button = QtWidgets.QPushButton(self.centralwidget)
        self.Test_3Button.setGeometry(QtCore.QRect(40, 290, 300, 51))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(22)
        self.Test_3Button.setFont(font)
        self.Test_3Button.setObjectName("Test_3Button")
        self.Test_3Button.setStyleSheet("background-color: #F6ED9A")

        self.Test_4Button = QtWidgets.QPushButton(self.centralwidget)
        self.Test_4Button.setGeometry(QtCore.QRect(40, 370, 300, 51))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(22)
        self.Test_4Button.setFont(font)
        self.Test_4Button.setObjectName("Test_4Button")
        self.Test_4Button.setStyleSheet("background-color: #F6ED9A")

        self.Test_5Button = QtWidgets.QPushButton(self.centralwidget)
        self.Test_5Button.setGeometry(QtCore.QRect(40, 450, 300, 51))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(22)
        self.Test_5Button.setFont(font)
        self.Test_5Button.setObjectName("Test_5Button")
        self.Test_5Button.setStyleSheet("background-color: #F6ED9A")

        View_4.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(View_4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 22))
        self.menubar.setObjectName("menubar")
        View_4.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(View_4)
        self.statusbar.setObjectName("statusbar")
        View_4.setStatusBar(self.statusbar)

        self.retranslateUi(View_4)
        QtCore.QMetaObject.connectSlotsByName(View_4)

    def retranslateUi(self, View_4):
        _translate = QtCore.QCoreApplication.translate
        View_4.setWindowTitle(_translate("View_4", "View_4"))
        self.TestsLabel.setText(_translate("View_4", "Тесты"))
        self.Test_1Button.setText(_translate("View_4", "Тест 1. Conditional Sentences"))
        self.Test_2Button.setText(_translate("View_4", "Тест 2"))
        self.Test_3Button.setText(_translate("View_4", "Тест 3"))
        self.Test_4Button.setText(_translate("View_4", "Тест 4"))
        self.Test_5Button.setText(_translate("View_4", "Тест 5"))

        pixmap = QPixmap("./img/backNarrow.png")
        self.NackNarrowImage.setPixmap(pixmap)

        def clickTest1Description():
            self.DescriptionTextBrowser.setHtml(_translate("View_4",
                                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                           "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Тест направлен на закрепление знаний по теме </span><span style=\" font-size:24pt; font-weight:600;\">Conditional Sentences</span></p></body></html>"))

        def clickTest2Description():
            self.DescriptionTextBrowser.setHtml(_translate("View_4",
                                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                           "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Описание </span><span style=\" font-size:24pt; font-weight:600;\">теста 2</span></p></body></html>"))

        def clickTest3Description():
            self.DescriptionTextBrowser.setHtml(_translate("View_4",
                                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                           "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Описание </span><span style=\" font-size:24pt; font-weight:600;\">теста 3</span></p></body></html>"))

        def clickTest4Description():
            self.DescriptionTextBrowser.setHtml(_translate("View_4",
                                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                           "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Описание </span><span style=\" font-size:24pt; font-weight:600;\">теста 4</span></p></body></html>"))

        def clickTest5Description():
            self.DescriptionTextBrowser.setHtml(_translate("View_4",
                                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                           "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Описание </span><span style=\" font-size:24pt; font-weight:600;\">теста 5</span></p></body></html>"))

        self.Test_1Button.clicked.connect(clickTest1Description)
        self.Test_2Button.clicked.connect(clickTest2Description)
        self.Test_3Button.clicked.connect(clickTest3Description)
        self.Test_4Button.clicked.connect(clickTest4Description)
        self.Test_5Button.clicked.connect(clickTest5Description)
