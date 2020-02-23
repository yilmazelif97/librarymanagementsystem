import sqlite3

from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from usereditpage import Ui_useredit

from usermainpage import Ui_usermain


dbase = sqlite3.connect('library.db')


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, QDate


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_issuereturn(object):

    def addborrow(self, issuereturn):

        bookıd = self.textEdit_3.toPlainText()
        userıd = self.textEdit_2.toPlainText()
        issueıd = self.textEdit.toPlainText()

        #print(bookıd)
        #print(userıd)
        #print(issueıd)

        borrowdate = self.textEdit_4.toPlainText()
        returndate = self.textEdit_6.toPlainText()



        silincek = self.textEdit_5.toPlainText()

        #print(borrowdate)
        #print(returndate)

        conn = sqlite3.connect('library.db')
        conn1 = conn.cursor()
        conn1.execute('''INSERT INTO borrow (ISSUEID,USERID,BOOKID,ISSUEDATE,RETURNDATE,BORROW) VALUES (?,?,?,?,?,?) ''',
                     (issueıd, userıd, bookıd, borrowdate, returndate,silincek))
        conn.commit()
        conn1.execute(''' update user set BOOKID = ? where USERID = ? ''', (bookıd,userıd))
        conn.commit()
        #a=conn2.execute('''SELECT FROM * user.USERID ''')
        #print(a)






        #result = QMessageBox.warning(issuereturn, 'Message', 'Borrowed Book!')
        #issuereturn.show()

        conn.commit()
        conn1.commit()


    def deneme(self):



        userıd = self.textEdit_2.toPlainText()
        bookıd = self.textEdit_3.toPlainText()

        connection = sqlite3.connect("library.db")
        c = connection.cursor()
        #query = c.execute(''' SELECT USERID FROM user ''')
        #result = query.fetchall()  # fetchone() veritabanındaki verileri sıralı şekilde almamı sağlıyor
        #fetchall() tüm USERID lerimin sırlı şekilde gelmesini sağlıyor aşağıdan yukarıya
        # tamam çalıştı tüm USERID lere ulaşabiliyorum

        #c.execute('''INSERT INTO u.BOOKID FROM user u, books b WHERE u.USERID=b.USERID  ''',bookıd)

        #a=c.execute(''' SELECT borrow.USERID FROM  borrow, user''')
        #b = a.fetchone()




        connection.commit()

    def getdate(self):

        date = QDate.currentDate()
        self.textEdit_4.setText(date.toString())


    def returndate(self):

        returndate = QDate.currentDate().addDays(7)
        self.textEdit_6.setText(returndate.toString())



    def returnbook(self):

            conn = sqlite3.connect('library.db')
            cur = conn.cursor()
            cur.execute("DELETE FROM borrow WHERE ISSUEID=? ", (self.textEdit_3.toPlainText() ))
            #result = QMessageBox.warning(issuereturn, 'Message', 'Returned Book!')
            #issuereturn.show()
            conn.commit()
            conn.close()

    def displaybooks(self):

        self.connection = sqlite3.connect("library.db")
        query = "SELECT * FROM borrow"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()




    def setupUi(self, issuereturn):
        issuereturn.setObjectName("issuereturn")
        issuereturn.resize(971, 740)
        issuereturn.setStyleSheet("background-image: url(ds.jpg);")
        self.textEdit = QtWidgets.QTextEdit(issuereturn)
        self.textEdit.setGeometry(QtCore.QRect(746, 380, 171, 41))
        self.textEdit.setStyleSheet("background: white;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(issuereturn)
        self.textEdit_2.setGeometry(QtCore.QRect(740, 280, 171, 41))
        self.textEdit_2.setStyleSheet("background: white;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(issuereturn)
        self.label_2.setGeometry(QtCore.QRect(790, 350, 91, 20))
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
        self.label_3.setGeometry(QtCore.QRect(790, 250, 71, 16))
        self.label_3.setStyleSheet("QLabel{\n"
"\n"
"background: beige;\n"
"\n"
" color: black;\n"
"    font-size: 18px;\n"
"\n"
"}")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(issuereturn)
        self.pushButton.setGeometry(QtCore.QRect(270, 580, 91, 31))
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
        self.pushButton.clicked.connect(lambda :self.addborrow(issuereturn))
        self.pushButton_2 = QtWidgets.QPushButton(issuereturn)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 680, 101, 31))
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
        self.pushButton_2.clicked.connect(self.returnbook)
        self.pushButton_3 = QtWidgets.QPushButton(issuereturn)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 640, 191, 28))
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
        self.pushButton_3.clicked.connect(self.deneme)
        self.label_6 = QtWidgets.QLabel(issuereturn)
        self.label_6.setGeometry(QtCore.QRect(790, 450, 91, 20))
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
        self.textEdit_5.setGeometry(QtCore.QRect(740, 480, 171, 41))
        self.textEdit_5.setStyleSheet("background: white;")
        self.textEdit_5.setObjectName("textEdit_5")
        self.tableWidget = QtWidgets.QTableWidget(issuereturn)
        self.tableWidget.setGeometry(QtCore.QRect(50, 320, 601, 241))
        self.tableWidget.setStyleSheet("background: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)

        self.pushButton_4 = QtWidgets.QPushButton(issuereturn)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 640, 101, 28))
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
        self.pushButton_4.clicked.connect(self.displaybooks)
        self.textEdit_3 = QtWidgets.QTextEdit(issuereturn)
        self.textEdit_3.setGeometry(QtCore.QRect(740, 180, 171, 41))
        self.textEdit_3.setStyleSheet("background: white;")
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_8 = QtWidgets.QLabel(issuereturn)
        self.label_8.setGeometry(QtCore.QRect(780, 150, 91, 20))
        self.label_8.setStyleSheet("QLabel{\n"
"\n"
"background: beige;\n"
"\n"
" color: black;\n"
"    font-size: 18px;\n"
"\n"
"}")
        self.label_8.setObjectName("label_8")
        self.pushButton_5 = QtWidgets.QPushButton(issuereturn)
        self.pushButton_5.clicked.connect(self.getdate)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 100, 201, 61))
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
        self.pushButton_6 = QtWidgets.QPushButton(issuereturn)
        self.pushButton_6.clicked.connect(self.returndate)
        self.pushButton_6.setGeometry(QtCore.QRect(360, 100, 201, 61))
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
        self.textEdit_4 = QtWidgets.QTextEdit(issuereturn)
        self.textEdit_4.setGeometry(QtCore.QRect(50, 230, 221, 41))
        self.textEdit_4.setStyleSheet("background: white;")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_6 = QtWidgets.QTextEdit(issuereturn)
        self.textEdit_6.setGeometry(QtCore.QRect(360, 230, 221, 41))
        self.textEdit_6.setStyleSheet("background: white;")
        self.textEdit_6.setObjectName("textEdit_6")

        self.retranslateUi(issuereturn)
        QtCore.QMetaObject.connectSlotsByName(issuereturn)

    def retranslateUi(self, issuereturn):
        _translate = QtCore.QCoreApplication.translate
        issuereturn.setWindowTitle(_translate("issuereturn", "Issue/return page"))
        self.label_2.setText(_translate("issuereturn", "BookID"))
        self.label_3.setText(_translate("issuereturn", "UserID"))
        self.pushButton.setText(_translate("issuereturn", "Issue"))
        self.pushButton_2.setText(_translate("issuereturn", "Return"))
        self.pushButton_3.setText(_translate("issuereturn", "Turn Back Main Page"))
        self.label_6.setText(_translate("issuereturn", "Borrow"))
        self.pushButton_4.setText(_translate("issuereturn", "DISPLAY"))
        self.label_8.setText(_translate("issuereturn", "IssueID"))
        self.pushButton_5.setText(_translate("issuereturn", "Borrow Date"))
        self.pushButton_6.setText(_translate("issuereturn", "Return Date"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("issuereturn", "ISSUEID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("issuereturn", "USERID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("issuereturn", "BOOKID"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("issuereturn", "ISSUEDATE"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("issuereturn", "RETURNDATE"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("issuereturn", "BORROW"))


#import lili_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    issuereturn = QtWidgets.QWidget()
    ui = Ui_issuereturn()
    ui.setupUi(issuereturn)
    issuereturn.show()
    sys.exit(app.exec_())
