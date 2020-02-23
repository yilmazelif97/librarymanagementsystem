import sqlite3

from bookeditpage import Ui_bookedit
#from mainlogin import Ui_mainform
from usereditpage import Ui_useredit
from ıssuereturnpage import Ui_issuereturn

dbase = sqlite3.connect('library.db')



from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_adminmain(object):

    def openuseredit(self):

        self.useredit = QtWidgets.QMainWindow()
        self.ui = Ui_useredit()
        self.ui.setupUi(self.useredit)
        self.useredit.show()

    def openbookedit(self):

        self.bookedit = QtWidgets.QMainWindow()
        self.ui = Ui_bookedit()
        self.ui.setupUi(self.bookedit)
        self.bookedit.show()

    def issuereturnedit(self):
        self.issuereturn = QtWidgets.QMainWindow()
        self.ui = Ui_issuereturn()
        self.ui.setupUi(self.issuereturn)
        self.issuereturn.show()

    def mainlogin(self):
        self.mainform = QtWidgets.QMainWindow()
        self.ui = Ui_mainform()
        self.ui.setupUi(self.mainform)
        self.mainform.show()



    def setupUi(self, adminmain):
        adminmain.setObjectName("adminmain")
        adminmain.resize(527, 535)
        adminmain.setStyleSheet("\n"
"\n"
"background-image: url(ds.jpg);")
        self.pushButton = QtWidgets.QPushButton(adminmain)
        self.pushButton.setGeometry(QtCore.QRect(190, 410, 151, 71))
        self.pushButton.setStyleSheet("QPushButton {\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"text-decoration: none;\n"
"background: #ffffff;\n"
"padding: 20px;\n"
"border: 4px solid #494949 !important;\n"
"display: inline-block;\n"
"transition: all 0.4s ease 0s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #ffffff !important;\n"
"background: #f6b93b;\n"
"border-color: #f6b93b !important;\n"
"transition: all 0.4s ease 0s;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.mainlogin)

        self.pushButton_2 = QtWidgets.QPushButton(adminmain)

        self.pushButton_2.clicked.connect(self.openbookedit)

        self.pushButton_2.setGeometry(QtCore.QRect(180, 90, 171, 81))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"text-decoration: none;\n"
"background: #ffffff;\n"
"padding: 20px;\n"
"border: 4px solid #494949 !important;\n"
"display: inline-block;\n"
"transition: all 0.4s ease 0s;\n"
"       \n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #ffffff !important;\n"
"background: #f6b93b;\n"
"border-color: #f6b93b !important;\n"
"transition: all 0.4s ease 0s;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(adminmain)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 200, 191, 71))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"text-decoration: none;\n"
"background: #ffffff;\n"
"padding: 20px;\n"
"border: 4px solid #494949 !important;\n"
"display: inline-block;\n"
"transition: all 0.4s ease 0s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #ffffff !important;\n"
"background: #f6b93b;\n"
"border-color: #f6b93b !important;\n"
"transition: all 0.4s ease 0s;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.issuereturnedit)

        self.pushButton_4 = QtWidgets.QPushButton(adminmain)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 300, 151, 71))

        self.pushButton_4.clicked.connect(self.openuseredit)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"text-decoration: none;\n"
"background: #ffffff;\n"
"padding: 20px;\n"
"border: 4px solid #494949 !important;\n"
"display: inline-block;\n"
"transition: all 0.4s ease 0s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #ffffff !important;\n"
"background: #f6b93b;\n"
"border-color: #f6b93b !important;\n"
"transition: all 0.4s ease 0s;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(adminmain)
        QtCore.QMetaObject.connectSlotsByName(adminmain)

    def retranslateUi(self, adminmain):
        _translate = QtCore.QCoreApplication.translate
        adminmain.setWindowTitle(_translate("adminmain", "AdminMain Page"))
        self.pushButton.setText(_translate("adminmain", "Logout"))
        self.pushButton_2.setText(_translate("adminmain", "Books"))
        self.pushButton_3.setText(_translate("adminmain", "Issue/Return"))
        self.pushButton_4.setText(_translate("adminmain", "User"))
#import ş_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminmain = QtWidgets.QWidget()
    ui = Ui_adminmain()
    ui.setupUi(adminmain)
    adminmain.show()
    sys.exit(app.exec_())
