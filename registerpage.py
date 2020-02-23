import sqlite3

#from mainlogin import Ui_mainform

conn = sqlite3.connect('library.db')

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

dbase = sqlite3.connect('library.db')


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_registerpage(object):

    def data_entry(self):

        userıd = self.textEdit_6.toPlainText()
        username = self.textEdit.toPlainText()
        usersurname = self.textEdit_2.toPlainText()
        phonenumber = self.textEdit_3.toPlainText()
        userloginname = self.textEdit_4.toPlainText()
        password = self.textEdit_5.toPlainText()
        conn = sqlite3.connect('library.db')
        conn.execute( ''' INSERT INTO user (USERID,USERNAME, USERSURNAME, PHONENUMBER, USERLOGINNAME, PASSWORD) VALUES (?,?,?,?,?,?) ''', (userıd,username, usersurname, phonenumber, userloginname, password))
        conn.commit()


    def mainopen(self):
        self.mainlogin = QtWidgets.QMainWindow()
        self.ui = Ui_mainform()
        self.ui.setupUi(self.mainlogin)
        self.mainlogin.show()

    def setupUi(self, registerpage):
        registerpage.setObjectName("registerpage")
        registerpage.resize(605, 576)
        registerpage.setStyleSheet("QWidget{\n"
"    background-image: url(yp.jpg);\n"
"\n"
"}")
        self.label = QtWidgets.QLabel(registerpage)
        self.label.setGeometry(QtCore.QRect(110, 200, 55, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(registerpage)
        self.label_2.setGeometry(QtCore.QRect(90, 240, 101, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(registerpage)
        self.label_3.setGeometry(QtCore.QRect(60, 290, 151, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(registerpage)
        self.label_4.setGeometry(QtCore.QRect(64, 330, 121, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(registerpage)
        self.label_5.setGeometry(QtCore.QRect(74, 390, 111, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(registerpage)
        self.textEdit.setGeometry(QtCore.QRect(240, 190, 201, 31))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"\n"
"background:white;\n"
"\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(registerpage)
        self.textEdit_2.setGeometry(QtCore.QRect(240, 240, 201, 31))
        self.textEdit_2.setStyleSheet("QTextEdit{\n"
"\n"
"background:white;\n"
"\n"
"}")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(registerpage)
        self.textEdit_3.setGeometry(QtCore.QRect(240, 290, 201, 31))
        self.textEdit_3.setStyleSheet("QTextEdit{\n"
"\n"
"background:white;\n"
"\n"
"}")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(registerpage)
        self.textEdit_4.setGeometry(QtCore.QRect(240, 340, 201, 31))
        self.textEdit_4.setStyleSheet("QTextEdit{\n"
"\n"
"background:white;\n"
"\n"
"}")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(registerpage)
        self.textEdit_5.setGeometry(QtCore.QRect(240, 390, 201, 31))
        self.textEdit_5.setStyleSheet("QTextEdit{\n"
"\n"
"background:white;\n"
"\n"
"}")
        self.textEdit_5.setObjectName("textEdit_5")
        self.pushButton = QtWidgets.QPushButton(registerpage)
        self.pushButton.setGeometry(QtCore.QRect(350, 470, 121, 51))
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
        self.pushButton.clicked.connect(self.data_entry)

        self.label_6 = QtWidgets.QLabel(registerpage)
        self.label_6.setGeometry(QtCore.QRect(180, 50, 211, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(registerpage)
        self.pushButton_2.clicked.connect(self.mainopen)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 470, 191, 51))
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
        self.label_7 = QtWidgets.QLabel(registerpage)
        self.label_7.setGeometry(QtCore.QRect(94, 150, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.textEdit_6 = QtWidgets.QTextEdit(registerpage)
        self.textEdit_6.setGeometry(QtCore.QRect(240, 140, 201, 31))
        self.textEdit_6.setStyleSheet("QTextEdit{\n"
"\n"
"background:white;\n"
"\n"
"}")
        self.textEdit_6.setObjectName("textEdit_6")

        self.retranslateUi(registerpage)
        QtCore.QMetaObject.connectSlotsByName(registerpage)

    def retranslateUi(self, registerpage):
        _translate = QtCore.QCoreApplication.translate
        registerpage.setWindowTitle(_translate("registerpage", "Register Page"))
        self.label.setText(_translate("registerpage", "Name"))
        self.label_2.setText(_translate("registerpage", "Surname"))
        self.label_3.setText(_translate("registerpage", "Phone Number"))
        self.label_4.setText(_translate("registerpage", "User Name"))
        self.label_5.setText(_translate("registerpage", "Password"))
        self.pushButton.setText(_translate("registerpage", "Login"))
        self.label_6.setText(_translate("registerpage", "Register Page"))
        self.pushButton_2.setText(_translate("registerpage", "Turn Back Main Page"))
        self.label_7.setText(_translate("registerpage", "UserID"))
#import lili_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registerpage = QtWidgets.QWidget()
    ui = Ui_registerpage()
    ui.setupUi(registerpage)
    registerpage.show()
    sys.exit(app.exec_())
