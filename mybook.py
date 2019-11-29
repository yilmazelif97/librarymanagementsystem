
import sqlite3

dbase = sqlite3.connect('library.db')


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_mybook(object):
    def setupUi(self, mybook):
        mybook.setObjectName("mybook")
        mybook.resize(587, 304)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        mybook.setFont(font)
        mybook.setStyleSheet("QWidget{\n"
"\n"
"    background-image: url(:/newPrefix/yp.jpg);\n"
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
        self.label_3 = QtWidgets.QLabel(mybook)
        self.label_3.setGeometry(QtCore.QRect(34, 186, 91, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
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
        self.textEdit_3 = QtWidgets.QTextEdit(mybook)
        self.textEdit_3.setGeometry(QtCore.QRect(150, 180, 161, 31))
        self.textEdit_3.setStyleSheet("QTextEdit{\n"
"\n"
"background: white;\n"
"\n"
"\n"
"}")
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton = QtWidgets.QPushButton(mybook)
        self.pushButton.setGeometry(QtCore.QRect(70, 230, 191, 51))
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
        self.plainTextEdit = QtWidgets.QPlainTextEdit(mybook)
        self.plainTextEdit.setGeometry(QtCore.QRect(320, 40, 261, 251))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        font.setItalic(False)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background:white\n"
";")
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(mybook)
        QtCore.QMetaObject.connectSlotsByName(mybook)

    def retranslateUi(self, mybook):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("mybook", "Book Name"))
        self.label_2.setText(_translate("mybook", "Return Date"))
        self.label_3.setText(_translate("mybook", "Dept"))
        self.pushButton.setText(_translate("mybook", "Turn Back Main Page"))
        self.plainTextEdit.setPlainText(_translate("mybook", "You can see the book you borrowed and the delivery date here. You must return the book within 14 days of the date you borrowed it. If you have passed the refund date, you can also see the debt you have to pay to our library. Thank you for your sensitivity"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mybook = QtWidgets.QWidget()
    ui = Ui_mybook()
    ui.setupUi(mybook)
    mybook.show()
    sys.exit(app.exec_())
