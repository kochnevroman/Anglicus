from PyQt5 import QtWidgets
from view_1 import Ui_View_1
from view_2 import Ui_View_2
from view_3 import Ui_View_3
from view_4 import Ui_View_4
from view_5 import Ui_View_5
import sys

import pyodbc

server = 'den1.mssql8.gear.host'
db = 'englishteacher'
usr = 'englishteacher'
psword = 'Rt0b2!c9Um_i'

conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=' + server + ';'
                                                                                  'DATABASE=' + db + ';UID=' + usr + ';PWD=' + psword)
cursor = conn.cursor()





class mywindow(QtWidgets.QMainWindow):
    def goView_2(self):
        self.ui = Ui_View_2()
        self.ui.setupUi(self)
        self.ui.NackNarrowImage.mousePressEvent = self.NackNarrowImageClickedToView_1
        self.ui.TestsButton.clicked.connect(self.goView_3)
        self.ui.DictButton.clicked.connect(self.goView_5)

    def goView_3(self):
        self.ui = Ui_View_3()
        self.ui.setupUi(self)
        self.ui.NackNarrowImage.mousePressEvent = self.NackNarrowImageClickedToView_2
        self.ui.StandardTestButton.clicked.connect(self.goView_4)

    def goView_4(self):
        self.ui = Ui_View_4()
        self.ui.setupUi(self)
        self.ui.NackNarrowImage.mousePressEvent = self.NackNarrowImageClickedToView_3

    def goView_5(self):
        self.ui = Ui_View_5()
        self.ui.setupUi(self)
        self.ui.NackNarrowImage.mousePressEvent = self.NackNarrowImageClickedToView_2

    def NackNarrowImageClickedToView_3(self, eve):
        self.ui = Ui_View_3()
        self.ui.setupUi(self)
        self.ui.NackNarrowImage.mousePressEvent = self.NackNarrowImageClickedToView_2
        self.ui.StandardTestButton.clicked.connect(self.goView_4)

    def NackNarrowImageClickedToView_2(self, eve):
        self.ui = Ui_View_2()
        self.ui.setupUi(self)
        self.ui.NackNarrowImage.mousePressEvent = self.NackNarrowImageClickedToView_1
        self.ui.TestsButton.clicked.connect(self.goView_3)
        self.ui.DictButton.clicked.connect(self.goView_5)

    def NackNarrowImageClickedToView_1(self, eve):
        self.ui = Ui_View_1()
        self.ui.setupUi(self)
        self.ui.EnterButton.clicked.connect(self.goView_2)

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_View_1()
        self.ui.setupUi(self)
        self.ui.EnterButton.clicked.connect(self.goView_2)




app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())