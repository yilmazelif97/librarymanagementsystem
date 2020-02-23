import sqlite3

dbase = sqlite3.connect('library.db')


from PyQt5 import QtCore, QtGui, QtWidgets

from userlogin import Ui_userlogin



class Ui_mybook(object):

    def __init__(self, userID, data):
        self.userID = userID
        self.data = data

    def setupUi(self, mybook):
        mybook.setObjectName("mybook")
        mybook.resize(354, 304)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        mybook.setFont(font)
        mybook.setStyleSheet("QWidget{\n"
"\n"
"    background-image: url(yp.jpg);\n"
"\n"
"}")
        self.label = QtWidgets.QLabel(mybook)
        self.label.setGeometry(QtCore.QRect(20, 70, 111, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(mybook)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 121, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(mybook)
        self.textEdit.setGeometry(QtCore.QRect(150, 70, 161, 31))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"\n"
"background: white;\n"
"\n"
"\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(mybook)
        self.textEdit_2.setGeometry(QtCore.QRect(150, 120, 161, 31))
        self.textEdit_2.setStyleSheet("QTextEdit{\n"
"\n"
"background: white;\n"
"\n"
"\n"
"}")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(mybook)
        self.pushButton.setGeometry(QtCore.QRect(70, 220, 191, 51))
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

        self.retranslateUi(mybook)
        QtCore.QMetaObject.connectSlotsByName(mybook)

    def retranslateUi(self, mybook):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("mybook", "Book ID"))
        self.label_2.setText(_translate("mybook", "Return Date"))
        self.pushButton.setText(_translate("mybook", "Turn Back Main Page"))

        self.textEdit.setText(str(self.data['BOOKID']))
        self.textEdit_2.setText(str(self.data['RETURNDATE']))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mybook = QtWidgets.QWidget()
    ui = Ui_mybook()
    ui.setupUi(mybook)
    mybook.show()
    sys.exit(app.exec_())
