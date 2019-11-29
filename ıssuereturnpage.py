
import sqlite3

dbase = sqlite3.connect('library.db')


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_issuereturn(object):
    def setupUi(self, issuereturn):
        issuereturn.setObjectName("issuereturn")
        issuereturn.resize(867, 629)
        issuereturn.setStyleSheet("background-image: url(:/newPrefix/ds.jpg);")
        self.textEdit = QtWidgets.QTextEdit(issuereturn)
        self.textEdit.setGeometry(QtCore.QRect(666, 170, 171, 41))
        self.textEdit.setStyleSheet("background: white;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(issuereturn)
        self.textEdit_2.setGeometry(QtCore.QRect(660, 70, 171, 41))
        self.textEdit_2.setStyleSheet("background: white;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.listView = QtWidgets.QListView(issuereturn)
        self.listView.setGeometry(QtCore.QRect(20, 350, 601, 231))
        self.listView.setStyleSheet("background: white;")
        self.listView.setObjectName("listView")
        self.label_2 = QtWidgets.QLabel(issuereturn)
        self.label_2.setGeometry(QtCore.QRect(710, 140, 91, 20))
        self.label_2.setStyleSheet("QLabel{\n"
"\n"
"background: beige;\n"
"\n"
" color: black;\n"
"    font-size: 18px;\n"
"\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(issuereturn)
        self.label_3.setGeometry(QtCore.QRect(710, 40, 71, 16))
        self.label_3.setStyleSheet("QLabel{\n"
"\n"
"background: beige;\n"
"\n"
" color: black;\n"
"    font-size: 18px;\n"
"\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(issuereturn)
        self.label_4.setGeometry(QtCore.QRect(120, 40, 111, 16))
        self.label_4.setStyleSheet("QLabel{\n"
"\n"
"background: beige;\n"
"\n"
" color: black;\n"
"    font-size: 18px;\n"
"\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(issuereturn)
        self.label_5.setGeometry(QtCore.QRect(390, 40, 121, 16))
        self.label_5.setStyleSheet("QLabel{\n"
"\n"
"background: beige;\n"
"\n"
" color: black;\n"
"    font-size: 18px;\n"
"\n"
"}")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(issuereturn)
        self.pushButton.setGeometry(QtCore.QRect(700, 360, 93, 28))
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
        self.pushButton_2 = QtWidgets.QPushButton(issuereturn)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 420, 101, 31))
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
        self.pushButton_3 = QtWidgets.QPushButton(issuereturn)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 480, 191, 28))
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
        self.label_6 = QtWidgets.QLabel(issuereturn)
        self.label_6.setGeometry(QtCore.QRect(710, 240, 91, 20))
        self.label_6.setStyleSheet("QLabel{\n"
"\n"
"background: beige;\n"
"\n"
" color: black;\n"
"    font-size: 18px;\n"
"\n"
"}")
        self.label_6.setObjectName("label_6")
        self.textEdit_5 = QtWidgets.QTextEdit(issuereturn)
        self.textEdit_5.setGeometry(QtCore.QRect(660, 270, 171, 41))
        self.textEdit_5.setStyleSheet("background: white;")
        self.textEdit_5.setObjectName("textEdit_5")
        self.calendarWidget = QtWidgets.QCalendarWidget(issuereturn)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 80, 291, 241))
        self.calendarWidget.setStyleSheet("background: white;\n"
"color:black;")
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(issuereturn)
        self.calendarWidget_2.setGeometry(QtCore.QRect(330, 80, 291, 241))
        self.calendarWidget_2.setStyleSheet("background: white;\n"
"color:black;")
        self.calendarWidget_2.setObjectName("calendarWidget_2")

        self.retranslateUi(issuereturn)
        QtCore.QMetaObject.connectSlotsByName(issuereturn)

    def retranslateUi(self, issuereturn):
        _translate = QtCore.QCoreApplication.translate
        issuereturn.setWindowTitle(_translate("issuereturn", "Issue/return page"))
        self.label_2.setText(_translate("issuereturn", "BookID"))
        self.label_3.setText(_translate("issuereturn", "UserID"))
        self.label_4.setText(_translate("issuereturn", "Issue Date"))
        self.label_5.setText(_translate("issuereturn", "Return Date"))
        self.pushButton.setText(_translate("issuereturn", "Issue"))
        self.pushButton_2.setText(_translate("issuereturn", "Return"))
        self.pushButton_3.setText(_translate("issuereturn", "Turn Back Main Page"))
        self.label_6.setText(_translate("issuereturn", "Borrow"))
#import lili_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    issuereturn = QtWidgets.QWidget()
    ui = Ui_issuereturn()
    ui.setupUi(issuereturn)
    issuereturn.show()
    sys.exit(app.exec_())
