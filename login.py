import sys
import os
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette


# F6ED9A - yellow - (246, 237, 154)

def text_font_bold(label):
    font = QtGui.QFont("Times", 12)
    font.setBold(True)
    label.setFont(font)


def text_font(label):
    font = QtGui.QFont("Times", 12)
    label.setFont(font)


StyleSheet = '''
    QWidget{
        background-color:#fff;
    }
    QLineEdit{
        border-width: 1px;
        border-color: #000;
        border-style: outset;
        border-width: 3px;
        border-radius: 3px;
    }
    QLabel{
        font-size: 12pt;
        
    }
    QPushButton {
        border-width: 1px;
        border-color: #000;
        border-style: outset;
        border-width: 3px;
        border-radius: 3px;
        font-size: 10pt;
    }
    QPushButton#YellowButton {
        background-color: #F6ED9A;
        color: #000000
    }
    #YellowButton:hover {
        background-color: #000000; 
        color: #fff;
    }
    QPlainTextEdit{
        font-size: 12pt;
    }
    QPlainTextEdit#text{
        color:#000;
        background-color: #fff;
        border: none;
    }
    QLabel{
        
    }
    '''

path_queen_icon = '..//images//queen_icon.png'


def login():
    app = QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    window = QWidget()
    window.setWindowTitle("Anglicus")
    window.setGeometry(300, 300, 1000, 800)  # положение окна х, у, ширина, высота
    window.setWindowIcon(QtGui.QIcon(path_queen_icon))

    grid = QGridLayout(window)

    # lEFT SIDE
    # ANGLICUS
    label_anglicus = QLabel("Anglicus")
    label_anglicus.setAlignment(Qt.AlignCenter)
    text_font((label_anglicus))

    # LOGIN
    label_login = QLabel("Логин")
    text_font(label_login)
    enter_login = QLineEdit()

    # PASSWORD
    label_password = QLabel("Пароль")
    label_password.setAlignment(Qt.AlignLeft)
    text_font(label_password)
    enter_password = QLineEdit()

    # ENTER BUTTON
    enter = QPushButton("Вход", objectName="YellowButton", minimumHeight=50)

    # RIGHT SIDE
    icon = QtGui.QIcon(path_queen_icon)
    text = QPlainTextEdit(
        "Anglicus - это бесплатное приложение, которое поможет освоить основы грамматики и лексики "
        "по английскому языку. Совершенствуйся вместе с нами!", objectName="text")
    text.setReadOnly(True)

    grid.addWidget(label_anglicus, 0, 0)
    grid.addWidget(label_login, 1, 0)
    grid.addWidget(enter_login, 2, 0)
    grid.addWidget(text, 1, 1, 4, 1)  # с 1 строки 1 столбца до 4 строки 1 столбца
    grid.addWidget(label_password, 3, 0)
    grid.addWidget(enter_password, 4, 0)
    grid.addWidget(enter, 5, 0)
    grid.setSpacing(10)

    window.show()
    sys.exc_info(app.exec_())


login()
