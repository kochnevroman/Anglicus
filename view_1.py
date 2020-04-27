# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap



class Ui_View_1(object):

    def setupUi(self, View_1):
        View_1.setObjectName("First View")
        View_1.resize(715, 565)
        self.centralwidget = QtWidgets.QWidget(View_1)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #fff")

        self.EnterButton = QtWidgets.QPushButton(self.centralwidget)
        self.EnterButton.setGeometry(QtCore.QRect(90, 390, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.EnterButton.setFont(font)
        self.EnterButton.setAutoFillBackground(False)
        self.EnterButton.setCheckable(False)
        self.EnterButton.setAutoRepeat(False)
        self.EnterButton.setObjectName("EnterButton")
        self.EnterButton.setStyleSheet('''
                                        background-color: #F6ED9A;
                                        border-color: #000;
                                        border-style: outset;
                                        border-width: 2px;
                                        border-radius: 5px;
        ''')

        self.LoginEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LoginEdit.setGeometry(QtCore.QRect(70, 190, 251, 35))
        self.LoginEdit.setObjectName("LoginEdit")
        self.LoginEdit.setStyleSheet('''
                                        background-color: #faf5c8;
                                        border-width: 1px;
                                        border-color: #000;
                                        border-style: outset;
                                        border-width: 1px;
                                        border-radius: 5px;
        ''')

        self.PasswordEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordEdit.setGeometry(QtCore.QRect(70, 290, 251, 35))
        self.PasswordEdit.setObjectName("PasswordEdit")
        self.PasswordEdit.setStyleSheet('''
                                             background-color: #faf5c8;
                                             border-width: 1px;
                                             border-color: #000;
                                             border-style: outset;
                                             border-width: 1px;
                                             border-radius: 5px;
                                        ''')

        self.DescriptiontextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.DescriptiontextBrowser.setGeometry(QtCore.QRect(430, 190, 256, 241))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.DescriptiontextBrowser.setFont(font)
        self.DescriptiontextBrowser.setLineWidth(0)
        self.DescriptiontextBrowser.setObjectName("DescriptiontextBrowser")
        self.DescriptiontextBrowser.setStyleSheet('''
                                                                    background-color: #fff;
                                                                    border: none;
                                                                    ''')

        self.LoginLabel = QtWidgets.QLabel(self.centralwidget)
        self.LoginLabel.setGeometry(QtCore.QRect(70, 160, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.LoginLabel.setFont(font)
        self.LoginLabel.setObjectName("LoginLabel")
        self.LoginLabel.setStyleSheet("background-color: #F6ED9A")

        self.AnglicusLabel = QtWidgets.QLabel(self.centralwidget)
        self.AnglicusLabel.setGeometry(QtCore.QRect(140, 50, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(30)
        self.AnglicusLabel.setFont(font)
        self.AnglicusLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AnglicusLabel.setAutoFillBackground(False)
        self.AnglicusLabel.setObjectName("AnglicusLabel")
        self.AnglicusLabel.setStyleSheet("background-color: #F6ED9A")

        self.PasswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.PasswordLabel.setGeometry(QtCore.QRect(70, 260, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.PasswordLabel.setFont(font)
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.PasswordLabel.setStyleSheet("background-color: #F6ED9A")

        self.QueenLogo = QtWidgets.QLabel(self.centralwidget)
        self.QueenLogo.setGeometry(QtCore.QRect(430, 20, 111, 121))
        self.QueenLogo.setObjectName("QueenLogo")

        self.Pallet = QtWidgets.QLabel(self.centralwidget)
        self.Pallet.setGeometry(QtCore.QRect(20, 20, 356, 491))
        self.Pallet.setAutoFillBackground(False)
        self.Pallet.setText("")
        self.Pallet.setObjectName("Pallet")
        self.Pallet.raise_()
        self.Pallet.setStyleSheet('''
                                             background-color: #F6ED9A;
                                             border-style: outset;
                                             border-color: #F6ED9A;
                                             border-width: 2px;
                                             border-radius: 10px;
             ''')

        self.EnterButton.raise_()
        self.LoginEdit.raise_()
        self.DescriptiontextBrowser.raise_()
        self.LoginLabel.raise_()
        self.AnglicusLabel.raise_()
        self.PasswordLabel.raise_()
        self.PasswordEdit.raise_()
        self.QueenLogo.raise_()
        View_1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(View_1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 22))
        self.menubar.setObjectName("menubar")
        View_1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(View_1)
        self.statusbar.setObjectName("statusbar")
        View_1.setStatusBar(self.statusbar)

        self.retranslateUi(View_1)
        QtCore.QMetaObject.connectSlotsByName(View_1)

    def retranslateUi(self, View_1):
        _translate = QtCore.QCoreApplication.translate
        View_1.setWindowTitle(_translate("View_1", "View_1"))
        self.EnterButton.setText(_translate("View_1", "Войти"))
        self.DescriptiontextBrowser.setHtml(_translate("View_1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Anglilus - это бесплатное приложение, которое поможет освоить основые грамматики и лексики по английскому языку. Совершенствуйся вместе с нами!</p></body></html>"))
        self.LoginLabel.setText(_translate("View_1", "Логин"))
        self.AnglicusLabel.setText(_translate("View_1", "Anglicus"))
        self.PasswordLabel.setText(_translate("View_1", "Пароль"))
        self.QueenLogo.setText(_translate("View_1", "TextLabel"))
        pixmap = QPixmap("./img/queen.jpg")
        self.QueenLogo.setPixmap(pixmap)
