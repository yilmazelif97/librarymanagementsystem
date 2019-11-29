import sqlite3
from tkinter import END

dbase = sqlite3.connect('library.db')


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_useredit(object):

    def getcursor(self):
        curosor_row = self.tableWidget.focus()
        contents = self.tableWidget.item(curosor_row)
        row=contents['values']
        self.textEdit.setText(row[0])
        self.textEdit_2.setText(row[1])
        self.textEdit_3.setText(row[2])
        self.textEdit_4.setText(row[3])
        self.textEdit_5.setText(row[4])
        self.textEdit_6.setText(row[5])



    def deleteuser(self):

            conn = sqlite3.connect('library.db')
            cur = conn.cursor()
            cur.execute("DELETE FROM user WHERE USERID=? ", (self.textEdit.toPlainText() ))
            result = QMessageBox.warning(useredit, 'Message', 'Deleted User!')
            useredit.show()
            conn.commit()
            conn.close()

    def updateuser(self):
        conn=sqlite3.connect('library.db')
        c=conn.cursor()
        conn.execute(
            ''' UPDATE  user SET USERNAME=?, USERSURNAME=?, PHONENUMBER=?, USERLOGINNAME=?, PASSWORD=? WHERE USERID = ? ''',
            ( self.textEdit_2.toPlainText() ,self.textEdit_3.toPlainText(), self.textEdit_4.toPlainText(),
              self.textEdit_5.toPlainText(), self.textEdit_6.toPlainText(),self.textEdit.toPlainText()))
        result = QMessageBox.warning(useredit, 'Message', 'Updated User!')
        conn.commit()
        useredit.show()
        conn.close()

    def searchuser(self):
        searchroll = ""
        searchroll = self.textEdit_7.toPlainText()
        try:
            conn = sqlite3.connect("library.db")
            c = conn.cursor()
            result = c.execute("SELECT * FROM user WHERE USERID=" + str(searchroll))
            row = result.fetchone()
            searchresult = str(row[0])
            self.textEdit.setText(searchresult)
            self.textEdit_2.setText(str(row[1]))
            self.textEdit_3.setText(str(row[2]))
            self.textEdit_4.setText(str(row[3]))
            self.textEdit_5.setText(str(row[4]))
            self.textEdit_6.setText(str(row[5]))

            conn.close()
        except Exception:
            print("Could not find user from database")


    def list(self):

        self.connection = sqlite3.connect("library.db")
        query = "SELECT * FROM user"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def adduser(self):

            userıd = self.textEdit.toPlainText()
            username = self.textEdit_2.toPlainText()
            usersurname = self.textEdit_3.toPlainText()
            phonenumber = self.textEdit_4.toPlainText()
            userloginname = self.textEdit_5.toPlainText()
            password = self.textEdit_6.toPlainText()
            conn = sqlite3.connect('library.db')
            conn.execute(
                ''' INSERT INTO user (USERID,USERNAME, USERSURNAME, PHONENUMBER, USERLOGINNAME, PASSWORD) VALUES (?,?,?,?,?,?) ''',
                (userıd, username, usersurname, phonenumber, userloginname, password))
            result = QMessageBox.warning(useredit, 'Message','Added User!')
            useredit.show()


            conn.commit()






    def setupUi(self, useredit):
        useredit.setObjectName("useredit")
        useredit.resize(802, 586)
        useredit.setStyleSheet("background-image: url(:/newPrefix/ds.jpg);")
        self.label = QtWidgets.QLabel(useredit)
        self.label.setGeometry(QtCore.QRect(89, 60, 71, 20))
        self.label.setStyleSheet("QLabel{\n"
"\n"
"\n"
" color: orange;\n"
"background: beige;\n"
"    font-size: 18px;\n"
"\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(useredit)
        self.label_2.setGeometry(QtCore.QRect(89, 120, 71, 20))
        self.label_2.setStyleSheet("QLabel{\n"
"\n"
"\n"
" color: orange;\n"
"    font-size: 18px;\n"
"background: beige;\n"
"\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(useredit)
        self.label_3.setGeometry(QtCore.QRect(75, 190, 111, 20))
        self.label_3.setStyleSheet("QLabel{\n"
"\n"
"\n"
" color: orange;\n"
"    font-size: 18px;\n"
"background: beige;\n"
"\n"
"\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(useredit)
        self.label_4.setGeometry(QtCore.QRect(45, 250, 121, 20))
        self.label_4.setStyleSheet("QLabel{\n"
"\n"
"\n"
" color: orange;\n"
"    font-size: 18px;\n"
"background: beige;\n"
"\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(useredit)
        self.label_5.setGeometry(QtCore.QRect(55, 320, 121, 20))
        self.label_5.setStyleSheet("QLabel{\n"
"\n"
"background: beige;\n"
"\n"
" color: orange;\n"
"    font-size: 18px;\n"
"\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(useredit)
        self.label_6.setGeometry(QtCore.QRect(65, 380, 111, 20))
        self.label_6.setStyleSheet("QLabel{\n"
"\n"
"background: beige;\n"
"\n"
" color: orange;\n"
"    font-size: 18px;\n"
"\n"
"}")
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(useredit)
        self.textEdit.setGeometry(QtCore.QRect(175, 50, 201, 31))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"\n"
"background: white;\n"
"\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(useredit)
        self.textEdit_2.setGeometry(QtCore.QRect(175, 120, 201, 31))
        self.textEdit_2.setStyleSheet("QTextEdit{\n"
"\n"
"background: white;\n"
"\n"
"}")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(useredit)
        self.textEdit_3.setGeometry(QtCore.QRect(175, 180, 201, 31))
        self.textEdit_3.setStyleSheet("QTextEdit{\n"
"\n"
"background: white;\n"
"\n"
"}")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(useredit)
        self.textEdit_4.setGeometry(QtCore.QRect(175, 240, 201, 31))
        self.textEdit_4.setStyleSheet("QTextEdit{\n"
"\n"
"background: white;\n"
"\n"
"}")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(useredit)
        self.textEdit_5.setGeometry(QtCore.QRect(175, 310, 201, 31))
        self.textEdit_5.setStyleSheet("QTextEdit{\n"
"\n"
"background: white;\n"
"\n"
"}")
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(useredit)
        self.textEdit_6.setGeometry(QtCore.QRect(175, 370, 201, 31))
        self.textEdit_6.setStyleSheet("QTextEdit{\n"
"\n"
"background: white;\n"
"\n"
"}")
        self.textEdit_6.setObjectName("textEdit_6")
        self.pushButton = QtWidgets.QPushButton(useredit)
        self.pushButton.setGeometry(QtCore.QRect(60, 450, 111, 71))

        self.pushButton.clicked.connect(self.adduser)

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
        self.pushButton_2 = QtWidgets.QPushButton(useredit)
        self.pushButton_2.clicked.connect(self.deleteuser)

        self.pushButton_2.setGeometry(QtCore.QRect(270, 450, 111, 71))
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
        self.pushButton_3 = QtWidgets.QPushButton(useredit)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 450, 111, 71))
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
        self.pushButton_3.clicked.connect(self.updateuser)

        self.pushButton_4 = QtWidgets.QPushButton(useredit)
        self.pushButton_4.clicked.connect(self.searchuser)

        self.pushButton_4.setGeometry(QtCore.QRect(415, 50, 101, 41))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"  -webkit-transition-duration: 0.4s; \n"
"  transition-duration: 0.4s;\n"
"background: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #4CAF50; \n"
"  color: white;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.textEdit_7 = QtWidgets.QTextEdit(useredit)
        self.textEdit_7.setGeometry(QtCore.QRect(535, 60, 161, 31))
        self.textEdit_7.setStyleSheet("QTextEdit{\n"
"\n"
"background: white;\n"
"\n"
"}")
        self.textEdit_7.setObjectName("textEdit_7")
        self.pushButton_5 = QtWidgets.QPushButton(useredit)

        self.pushButton_5.setGeometry(QtCore.QRect(330, 540, 191, 28))
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
        self.tableWidget = QtWidgets.QTableWidget(useredit)
        self.tableWidget.setGeometry(QtCore.QRect(410, 120, 301, 281))
        self.tableWidget.setStyleSheet("background: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item=QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0,item)
        item=QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)



        self.pushButton_6 = QtWidgets.QPushButton(useredit)
        self.pushButton_6.setGeometry(QtCore.QRect(640, 450, 111, 71))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
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
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(useredit)
        QtCore.QMetaObject.connectSlotsByName(useredit)

    def retranslateUi(self, useredit):
        _translate = QtCore.QCoreApplication.translate
        useredit.setWindowTitle(_translate("useredit", "User Edit Page"))
        self.label.setText(_translate("useredit", "UserID"))
        self.label_2.setText(_translate("useredit", "Name"))
        self.label_3.setText(_translate("useredit", "Surname"))
        self.label_4.setText(_translate("useredit", "Phone Number"))
        self.label_5.setText(_translate("useredit", "Username"))
        self.label_6.setText(_translate("useredit", "Password"))
        self.pushButton.setText(_translate("useredit", "Add"))
        self.pushButton_2.setText(_translate("useredit", "Delete"))
        self.pushButton_3.setText(_translate("useredit", "Update"))
        self.pushButton_4.setText(_translate("useredit", "Search"))
        self.pushButton_5.setText(_translate("useredit", "Turn Back Main Page"))
        self.pushButton_6.setText(_translate("useredit", "Display"))
        self.pushButton_6.clicked.connect(self.list)

        self.tableWidget.doubleClicked.connect(self.ticklanmisSatir)

        item=self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("useredit","USERID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("useredit", "USERNAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("useredit", "USERSURNAME"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("useredit", "PHONENUMBER"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("useredit", "USERLOGINNAME"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("useredit", "PASSWORD"))

    def ticklanmisSatir(self):
        print("Table clicked")
        self.tableWidget.

#import lili_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    useredit = QtWidgets.QWidget()
    ui = Ui_useredit()
    ui.setupUi(useredit)
    useredit.show()
    sys.exit(app.exec_())
