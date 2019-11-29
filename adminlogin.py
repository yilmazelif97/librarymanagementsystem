
import sqlite3

from adminmainpage import Ui_adminmain

dbase = sqlite3.connect('library.db')


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_adminlogin(object):

    def logincheck(self):
        adminusername = self.textEdit.toPlainText()
        password = self.textEdit_2.toPlainText()

        connection = sqlite3.connect('library.db')

        result = connection.execute(''' SELECT * FROM admin WHERE ADMINUSERNAME= ? AND ADMINPASS = ? ''',
                                    (adminusername, password))
        if (len(result.fetchall()) > 0):
            print("user found")
            self.adminmain = QtWidgets.QMainWindow()
            self.ui = Ui_adminmain()
            self.ui.setupUi(self.adminmain)
            self.adminmain.show()


        else:
            print("user not found")



    def setupUi(self, adminlogin):
        adminlogin.setObjectName("adminlogin")
        adminlogin.resize(498, 378)
        adminlogin.setStyleSheet("QWidget{\n"
"    background-image: url(:/newPrefix/ds.jpg);\n"
"\n"
"\n"
"}")
        self.label = QtWidgets.QLabel(adminlogin)
        self.label.setGeometry(QtCore.QRect(24, 120, 181, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"\n"
"color: black;\n"
"background: beige;\n"
"\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(adminlogin)
        self.label_2.setGeometry(QtCore.QRect(30, 210, 171, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"\n"
"color: black;\n"
"background: beige;\n"
"\n"
"}")
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(adminlogin)
        self.textEdit.setGeometry(QtCore.QRect(240, 110, 221, 31))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"\n"
"background:white;\n"
"\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(adminlogin)
        self.textEdit_2.setGeometry(QtCore.QRect(240, 200, 221, 31))
        self.textEdit_2.setStyleSheet("QTextEdit{\n"
"\n"
"background:white;\n"
"\n"
"}")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(adminlogin)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 290, 171, 81))

        self.pushButton_3.clicked.connect(self.logincheck)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(adminlogin)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 290, 171, 81))
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

        self.retranslateUi(adminlogin)
        QtCore.QMetaObject.connectSlotsByName(adminlogin)

    def retranslateUi(self, adminlogin):
        _translate = QtCore.QCoreApplication.translate
        adminlogin.setWindowTitle(_translate("adminlogin", "Admin Login Page"))
        self.label.setText(_translate("adminlogin", "Admin User Name"))
        self.label_2.setText(_translate("adminlogin", "Admin Password"))
        self.pushButton_3.setText(_translate("adminlogin", "Login"))
        self.pushButton_2.setText(_translate("adminlogin", "Turn Back "))
#import qrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminlogin = QtWidgets.QWidget()
    ui = Ui_adminlogin()
    ui.setupUi(adminlogin)
    adminlogin.show()
    sys.exit(app.exec_())
