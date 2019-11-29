
#It is for users not admin

import sqlite3

dbase = sqlite3.connect('library.db')

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_listofbook(object):
    def setupUi(self, listofbook):
        listofbook.setObjectName("listofbook")
        listofbook.resize(441, 421)
        listofbook.setStyleSheet("\n"
"QWidget{\n"
"background: url(:/newPrefix/yp.jpg);\n"
"}\n"
"")
        self.textEdit = QtWidgets.QTextEdit(listofbook)
        self.textEdit.setGeometry(QtCore.QRect(170, 60, 171, 31))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"\n"
"background:white;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.listView = QtWidgets.QListView(listofbook)
        self.listView.setGeometry(QtCore.QRect(15, 100, 371, 192))
        self.listView.setStyleSheet("QListView{\n"
"\n"
"background:white;\n"
"}\n"
"")
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(listofbook)
        self.pushButton.setGeometry(QtCore.QRect(20, 47, 121, 41))
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
        self.pushButton_2 = QtWidgets.QPushButton(listofbook)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 340, 191, 51))
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

        self.retranslateUi(listofbook)
        QtCore.QMetaObject.connectSlotsByName(listofbook)

    def retranslateUi(self, listofbook):
        _translate = QtCore.QCoreApplication.translate
        listofbook.setWindowTitle(_translate("listofbook", "Book List"))
        self.pushButton.setText(_translate("listofbook", "Search"))
        self.pushButton_2.setText(_translate("listofbook", "Turn Back Main Page"))
#import lili_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    listofbook = QtWidgets.QWidget()
    ui = Ui_listofbook()
    ui.setupUi(listofbook)
    listofbook.show()
    sys.exit(app.exec_())
