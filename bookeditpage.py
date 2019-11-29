import sqlite3

dbase = sqlite3.connect('library.db')


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bookedit(object):
    def setupUi(self, bookedit):
        bookedit.setObjectName("bookedit")
        bookedit.resize(668, 633)
        bookedit.setStyleSheet("QWidget{\n"
"\n"
"\n"
"    background-image: url(:/newPrefix/ds.jpg);\n"
"}")
        self.label = QtWidgets.QLabel(bookedit)
        self.label.setGeometry(QtCore.QRect(20, 110, 101, 21))
        self.label.setStyleSheet("QLabel{\n"
"\n"
"\n"
" color: blue;\n"
"background: beige;\n"
"    font-size: 18px;\n"
"\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(bookedit)
        self.label_2.setGeometry(QtCore.QRect(30, 170, 101, 20))
        self.label_2.setStyleSheet("QLabel{\n"
"\n"
"background: beige;\n"
"\n"
" color: blue;\n"
"    font-size: 18px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(bookedit)
        self.label_3.setGeometry(QtCore.QRect(30, 280, 101, 20))
        self.label_3.setStyleSheet("QLabel{\n"
"\n"
"background: beige;\n"
"\n"
" color: blue;\n"
"    font-size: 18px;\n"
"\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(bookedit)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 121, 20))
        self.label_4.setStyleSheet("QLabel{\n"
"\n"
"background: beige;\n"
"\n"
" color: blue;\n"
"    font-size: 18px;\n"
"\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(bookedit)
        self.label_5.setGeometry(QtCore.QRect(30, 50, 91, 20))
        self.label_5.setStyleSheet("QLabel{\n"
"\n"
"background: beige;\n"
"\n"
" color: blue;\n"
"    font-size: 18px;\n"
"\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(bookedit)
        self.label_6.setGeometry(QtCore.QRect(10, 350, 121, 21))
        self.label_6.setStyleSheet("QLabel{\n"
"\n"
"background: beige;\n"
"\n"
" color: blue;\n"
"    font-size: 18px;\n"
"\n"
"}")
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(bookedit)
        self.textEdit.setGeometry(QtCore.QRect(150, 50, 161, 31))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"background: white;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(bookedit)
        self.textEdit_2.setGeometry(QtCore.QRect(150, 100, 161, 31))
        self.textEdit_2.setStyleSheet("QTextEdit{\n"
"background: white;\n"
"}")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(bookedit)
        self.textEdit_3.setGeometry(QtCore.QRect(150, 160, 161, 31))
        self.textEdit_3.setStyleSheet("QTextEdit{\n"
"background: white;\n"
"}")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(bookedit)
        self.textEdit_4.setGeometry(QtCore.QRect(150, 220, 161, 31))
        self.textEdit_4.setStyleSheet("QTextEdit{\n"
"background: white;\n"
"}")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(bookedit)
        self.textEdit_5.setGeometry(QtCore.QRect(150, 280, 161, 31))
        self.textEdit_5.setStyleSheet("QTextEdit{\n"
"background: white;\n"
"}")
        self.textEdit_5.setObjectName("textEdit_5")
        self.listView = QtWidgets.QListView(bookedit)
        self.listView.setGeometry(QtCore.QRect(340, 120, 281, 301))
        self.listView.setStyleSheet("QListView{\n"
"background: white;\n"
"}")
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(bookedit)
        self.pushButton.setGeometry(QtCore.QRect(340, 50, 101, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"  -webkit-transition-duration: 0.4s; \n"
"  transition-duration: 0.4s;\n"
"background: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #4CAF50; \n"
"  color: white;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.textEdit_7 = QtWidgets.QTextEdit(bookedit)
        self.textEdit_7.setGeometry(QtCore.QRect(450, 50, 161, 31))
        self.textEdit_7.setStyleSheet("QTextEdit{\n"
"background: white;\n"
"}")
        self.textEdit_7.setObjectName("textEdit_7")
        self.pushButton_2 = QtWidgets.QPushButton(bookedit)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 470, 101, 61))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(bookedit)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 470, 101, 61))
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
        self.pushButton_4 = QtWidgets.QPushButton(bookedit)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 470, 101, 61))
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
        self.pushButton_5 = QtWidgets.QPushButton(bookedit)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 560, 191, 28))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
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
        self.pushButton_5.setObjectName("pushButton_5")
        self.comboBox = QtWidgets.QComboBox(bookedit)
        self.comboBox.setGeometry(QtCore.QRect(150, 350, 161, 31))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(bookedit)
        QtCore.QMetaObject.connectSlotsByName(bookedit)

    def retranslateUi(self, bookedit):
        _translate = QtCore.QCoreApplication.translate
        bookedit.setWindowTitle(_translate("bookedit", "Book Edit Page"))
        self.label.setText(_translate("bookedit", "Book Name"))
        self.label_2.setText(_translate("bookedit", "Book Author"))
        self.label_3.setText(_translate("bookedit", "Book Page"))
        self.label_4.setText(_translate("bookedit", "Book Publisher"))
        self.label_5.setText(_translate("bookedit", "Book ID"))
        self.label_6.setText(_translate("bookedit", "Book Category"))
        self.pushButton.setText(_translate("bookedit", "Search"))
        self.pushButton_2.setText(_translate("bookedit", "Add"))
        self.pushButton_3.setText(_translate("bookedit", "Delete"))
        self.pushButton_4.setText(_translate("bookedit", "Update"))
        self.pushButton_5.setText(_translate("bookedit", "Turn Back Main Page"))
#import lili_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bookedit = QtWidgets.QWidget()
    ui = Ui_bookedit()
    ui.setupUi(bookedit)
    bookedit.show()
    sys.exit(app.exec_())
