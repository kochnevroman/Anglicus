# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'third_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_View_3(object):
    def setupUi(self, View_3):
        View_3.setObjectName("Third View")
        View_3.resize(715, 565)
        self.centralwidget = QtWidgets.QWidget(View_3)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #fff")

        self.Palet = QtWidgets.QLabel(self.centralwidget)
        self.Palet.setGeometry(QtCore.QRect(20, 20, 356, 491))
        self.Palet.setText("")
        self.Palet.setObjectName("Palet")
        self.Palet.setStyleSheet('''
                                             background-color: #F6ED9A;
                                             border-color: #F6ED9A;
                                             border-width: 2px;
                                             border-radius: 10px;
             ''')

        self.TestsLabel = QtWidgets.QLabel(self.centralwidget)
        self.TestsLabel.setGeometry(QtCore.QRect(146, 70, 71, 41))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(26)
        self.TestsLabel.setFont(font)
        self.TestsLabel.setObjectName("TestsLabel")
        self.TestsLabel.setStyleSheet("background-color: #F6ED9A")

        self.NackNarrowImage = QtWidgets.QLabel(self.centralwidget)
        self.NackNarrowImage.setGeometry(QtCore.QRect(40, 70, 51, 41))
        self.NackNarrowImage.setText("")
        self.NackNarrowImage.setObjectName("NackNarrowImage")
        self.NackNarrowImage.setStyleSheet("background-color: #F6ED9A")

        self.DescriptionTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.DescriptionTextBrowser.setGeometry(QtCore.QRect(420, 171, 256, 181))
        self.DescriptionTextBrowser.setObjectName("DescriptionTextBrowser")
        self.DescriptionTextBrowser.setStyleSheet('''
                                                            background-color: #fff;
                                                            border: none;
                                                            ''')

        self.StandardTestButton = QtWidgets.QPushButton(self.centralwidget)
        self.StandardTestButton.setGeometry(QtCore.QRect(90, 170, 191, 51))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(24)
        self.StandardTestButton.setFont(font)
        self.StandardTestButton.setObjectName("StandardTestButton")
        self.StandardTestButton.setStyleSheet("background-color: #F6ED9A")

        self.MediumTestButton = QtWidgets.QPushButton(self.centralwidget)
        self.MediumTestButton.setGeometry(QtCore.QRect(90, 250, 191, 51))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(24)
        self.MediumTestButton.setFont(font)
        self.MediumTestButton.setObjectName("MediumTestButton")
        self.MediumTestButton.setStyleSheet("background-color: #F6ED9A")

        self.HardTestButton = QtWidgets.QPushButton(self.centralwidget)
        self.HardTestButton.setGeometry(QtCore.QRect(90, 330, 191, 51))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(24)
        self.HardTestButton.setFont(font)
        self.HardTestButton.setObjectName("HardTestButton")
        self.HardTestButton.setStyleSheet("background-color: #F6ED9A")

        View_3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(View_3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 22))
        self.menubar.setObjectName("menubar")
        View_3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(View_3)
        self.statusbar.setObjectName("statusbar")
        View_3.setStatusBar(self.statusbar)

        self.retranslateUi(View_3)
        QtCore.QMetaObject.connectSlotsByName(View_3)

    def retranslateUi(self, View_3):
        _translate = QtCore.QCoreApplication.translate
        View_3.setWindowTitle(_translate("View_3", "View_3"))
        self.TestsLabel.setText(_translate("View_3", "Тесты"))
        self.DescriptionTextBrowser.setHtml(_translate("View_3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Тест содержит вопросы с выбором варианта ответа по заданной теме</span></p></body></html>"))
        self.StandardTestButton.setText(_translate("View_3", "Обычный"))
        self.MediumTestButton.setText(_translate("View_3", "Усложненный"))
        self.HardTestButton.setText(_translate("View_3", "Сложный"))

        pixmap = QPixmap("./img/backNarrow.png")
        self.NackNarrowImage.setPixmap(pixmap)