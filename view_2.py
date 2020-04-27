# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_View_2(object):
    def setupUi(self, View_1):
        View_1.setObjectName("Second View")
        View_1.resize(715, 565)
        self.centralwidget = QtWidgets.QWidget(View_1)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #fff")

        self.Pallet = QtWidgets.QLabel(self.centralwidget)
        self.Pallet.setGeometry(QtCore.QRect(20, 20, 381, 491))
        self.Pallet.setText("")
        self.Pallet.setObjectName("Pallet")
        self.Pallet.setStyleSheet('''
                                             background-color: #F6ED9A;
                                             border-color: #F6ED9A;
                                             border-width: 2px;
                                             border-radius: 10px;
             ''')

        self.NicknameLabel = QtWidgets.QLabel(self.centralwidget)
        self.NicknameLabel.setGeometry(QtCore.QRect(140, 110, 120, 31))
        self.NicknameLabel.setStyleSheet("background-color: #F6ED9A")

        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(26)
        self.NicknameLabel.setFont(font)
        self.NicknameLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.NicknameLabel.setObjectName("NicknameLabel")

        self.PrivateDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.PrivateDataButton.setGeometry(QtCore.QRect(105, 230, 191, 51))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(24)
        self.PrivateDataButton.setFont(font)
        self.PrivateDataButton.setObjectName("PrivateDataButton")
        self.PrivateDataButton.setStyleSheet('''
                                        background-color: #F6ED9A;
                                        border-color: #F6ED9A;
                                        border-style: outset;
                                        border-width: 0px;
                                        border-radius: 10px;
        ''')

        self.AchivButton = QtWidgets.QPushButton(self.centralwidget)
        self.AchivButton.setGeometry(QtCore.QRect(100, 340, 191, 51))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(24)
        self.AchivButton.setFont(font)
        self.AchivButton.setObjectName("AchivButton")
        self.AchivButton.setStyleSheet('''
                                        background-color: #F6ED9A;
                                        border-color: #F6ED9A;
                                        border-style: outset;
                                        border-width: 0px;
                                        border-radius: 10px;
        ''')

        self.TestsButton = QtWidgets.QPushButton(self.centralwidget)
        self.TestsButton.setGeometry(QtCore.QRect(450, 110, 191, 51))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(24)
        self.TestsButton.setFont(font)
        self.TestsButton.setObjectName("TestsButton")
        self.TestsButton.setStyleSheet('''
                                        border-color: #000;
                                        border-style: outset;
                                        border-width: 1px;
                                        border-radius: 10px;
        ''')

        self.GrammarButton = QtWidgets.QPushButton(self.centralwidget)
        self.GrammarButton.setGeometry(QtCore.QRect(450, 230, 191, 51))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(24)
        self.GrammarButton.setFont(font)
        self.GrammarButton.setObjectName("GrammarButton")
        self.GrammarButton.setStyleSheet('''
                                        border-color: #000;
                                        border-style: outset;
                                        border-width: 1px;
                                        border-radius: 10px;
        ''')

        self.DictButton = QtWidgets.QPushButton(self.centralwidget)
        self.DictButton.setGeometry(QtCore.QRect(450, 350, 191, 51))
        font = QtGui.QFont()
        font.setFamily(".Apple SD Gothic NeoI")
        font.setPointSize(24)
        self.DictButton.setFont(font)
        self.DictButton.setObjectName("DictButton")
        self.DictButton.setStyleSheet('''
                                        border-color: #000;
                                        border-style: outset;
                                        border-width: 1px;
                                        border-radius: 10px;
        ''')

        self.NackNarrowImage = QtWidgets.QLabel(self.centralwidget)
        self.NackNarrowImage.setGeometry(QtCore.QRect(40, 100, 51, 41))
        self.NackNarrowImage.setText("")
        self.NackNarrowImage.setObjectName("NackNarrowImage")
        self.NackNarrowImage.setStyleSheet("background-color: #F6ED9A")

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
        self.NicknameLabel.setText(_translate("View_1", "Hi, Donald!"))
        self.PrivateDataButton.setText(_translate("View_1", "Личные данные"))
        self.AchivButton.setText(_translate("View_1", "Достижения"))
        self.TestsButton.setText(_translate("View_1", "Тесты"))
        self.GrammarButton.setText(_translate("View_1", "Грамматика"))
        self.DictButton.setText(_translate("View_1", "Словарь"))

        pixmap = QPixmap("./img/backNarrow.png")
        self.NackNarrowImage.setPixmap(pixmap)
