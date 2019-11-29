
import sqlite3


dbase = sqlite3.connect('library.db')

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_usermain(object):



    def setupUi(self, usermain):
        usermain.setObjectName("usermain")
        usermain.resize(563, 530)
        usermain.setStyleSheet("\n"
"QWidget{\n"
"\n"
"    background-image: url(:/newPrefix/yp.jpg);\n"
"}")
        self.pushButton = QtWidgets.QPushButton(usermain)
        self.pushButton.setGeometry(QtCore.QRect(220, 130, 131, 91))
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

        self.pushButton_2 = QtWidgets.QPushButton(usermain)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 260, 121, 91))
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
        self.pushButton_3 = QtWidgets.QPushButton(usermain)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 400, 111, 71))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(usermain)
        self.label.setGeometry(QtCore.QRect(120, 40, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(18)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("background: ")
        self.label.setObjectName("label")

        self.retranslateUi(usermain)
        QtCore.QMetaObject.connectSlotsByName(usermain)

    def retranslateUi(self, usermain):
        _translate = QtCore.QCoreApplication.translate
        usermain.setWindowTitle(_translate("usermain", "User Main Page"))
        self.pushButton.setText(_translate("usermain", "List Of Books"))
        self.pushButton_2.setText(_translate("usermain", "My Book"))
        self.pushButton_3.setText(_translate("usermain", "Logout"))
        self.label.setText(_translate("usermain", "Welcome To User Page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    usermain = QtWidgets.QWidget()
    ui = Ui_usermain()
    ui.setupUi(usermain)
    usermain.show()
    sys.exit(app.exec_())
