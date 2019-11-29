import sqlite3

dbase = sqlite3.connect('library.db')

from usermainpage import Ui_usermain
from registerpage import Ui_registerpage



from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_userlogin(object):

    def openregister(self):

        self.registerpage = QtWidgets.QMainWindow()
        self.ui = Ui_registerpage()
        self.ui.setupUi(self.registerpage)
        self.registerpage.show()
        self.Form.close()

    def logincheck(self):
        userloginname = self.textEdit.toPlainText()
        password = self.textEdit_2.toPlainText()

        connection = sqlite3.connect('library.db')

        result = connection.execute(''' SELECT * FROM user WHERE userloginname = ? AND password = ? ''',
                                    (userloginname, password))
        if (len(result.fetchall()) > 0):
            print("user found")
            self.usermain = QtWidgets.QMainWindow()
            self.ui = Ui_usermain()
            self.ui.setupUi(self.usermain)
            self.usermain.show()


        else:
            print("user not found")

    def signupcheck(self):
        print("signupcheck button clicked")

    def setupUi(self, userlogin):

        self.Form = userlogin;


        userlogin.setObjectName("userlogin")
        userlogin.resize(425, 479)
        userlogin.setStyleSheet("QWidget{\n"
"\n"
"\n"
"    background-image: url(:/newPrefix/yp.jpg);\n"
"}")
        self.label = QtWidgets.QLabel(userlogin)
        self.label.setGeometry(QtCore.QRect(30, 110, 111, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(userlogin)
        self.label_2.setGeometry(QtCore.QRect(40, 200, 111, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(userlogin)
        self.textEdit.setGeometry(QtCore.QRect(160, 110, 191, 31))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"\n"
"background: white;\n"
"\n"
"}\n"
"\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(userlogin)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 190, 171, 31))
        self.textEdit_2.setStyleSheet("QTextEdit{\n"
"\n"
"background: white;\n"
"\n"
"}\n"
"\n"
"")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(userlogin)
        self.pushButton.clicked.connect(self.logincheck)
        self.pushButton.setGeometry(QtCore.QRect(70, 330, 111, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    color: white;\n"
"    background: #E9967A    ;\n"
"    padding: 10px 20px;\n"
"    cursor: pointer;\n"
"    border: 2px solid #E9967A    ;\n"
"    -moz-border-radius: 16px;\n"
"    -webkit-border-radius: 16px;\n"
"    border-radius: 16px;\n"
"}\n"
" \n"
"QPushButton:hover {\n"
"    color: #E9967A    ;\n"
"    background: #fff;\n"
"    border: 2px solid #E9967A    ;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(userlogin)
        self.pushButton_2.clicked.connect(self.openregister)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 330, 111, 41))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    color: white;\n"
"    background: #E9967A    ;\n"
"    padding: 10px 20px;\n"
"    cursor: pointer;\n"
"    border: 2px solid #E9967A    ;\n"
"    -moz-border-radius: 16px;\n"
"    -webkit-border-radius: 16px;\n"
"    border-radius: 16px;\n"
"}\n"
" \n"
"QPushButton:hover {\n"
"    color: #E9967A    ;\n"
"    background: #fff;\n"
"    border: 2px solid #E9967A    ;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(userlogin)
        self.label_3.setGeometry(QtCore.QRect(100, 40, 241, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(userlogin)
        QtCore.QMetaObject.connectSlotsByName(userlogin)

    def retranslateUi(self, userlogin):
        _translate = QtCore.QCoreApplication.translate
        userlogin.setWindowTitle(_translate("userlogin", "User Login Page"))
        self.label.setText(_translate("userlogin", "User Name"))
        self.label_2.setText(_translate("userlogin", "Password"))
        self.pushButton.setText(_translate("userlogin", "Login"))
        self.pushButton_2.setText(_translate("userlogin", "Register"))
        self.label_3.setText(_translate("userlogin", "User Login Page"))
#import lili_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    userlogin = QtWidgets.QWidget()
    ui = Ui_userlogin()
    ui.setupUi(userlogin)
    userlogin.show()
    sys.exit(app.exec_())
