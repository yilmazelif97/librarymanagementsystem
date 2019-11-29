


from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3

from PyQt5.QtGui import QIcon

dbase = sqlite3.connect('library.db')

class Ui_mainform(object):
    def setupUi(self, mainform):
        mainform.setObjectName("mainform")
        mainform.resize(776, 533)
        mainform.setMinimumSize(QtCore.QSize(0, 533))
        mainform.setAutoFillBackground(True)
        mainform.setStyleSheet("")
        self.label = QtWidgets.QLabel(mainform)
        self.label.setGeometry(QtCore.QRect(190, 60, 581, 71))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(mainform)
        self.pushButton.setGeometry(QtCore.QRect(130, 340, 122, 118))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"background-color: lightblue;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: double;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 20px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 110px;\n"
"max-width: 110px;\n"
"min-height: 110px;\n"
"max-height: 110px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(mainform)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 340, 122, 118))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"background-color: lightblue;\n"
"border-width: 1px;\n"
"border-color: #339;\n"
"border-style: double;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 20px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 110px;\n"
"max-width: 110px;\n"
"min-height: 110px;\n"
"max-height: 110px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(mainform)
        QtCore.QMetaObject.connectSlotsByName(mainform)

    def retranslateUi(self, mainform):
        _translate = QtCore.QCoreApplication.translate
        mainform.setWindowTitle(_translate("mainform", "Main Login Page"))
        self.label.setText(_translate("mainform", "Welcome To Ylw Library"))
        self.pushButton.setText(_translate("mainform", "Admin Login"))
        self.pushButton_2.setText(_translate("mainform", "User Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainform = QtWidgets.QWidget()
    ui = Ui_mainform()
    ui.setupUi(mainform)
    mainform.setWindowIcon(QIcon('li.jpg'))
    mainform.show()
    sys.exit(app.exec_())
