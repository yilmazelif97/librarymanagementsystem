import sqlite3

from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

dbase = sqlite3.connect('library.db')



from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bookedit(object):

    def listbook(self):

        self.connection = sqlite3.connect("library.db")
        query = "SELECT * FROM books"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def searchbook(self):
        searchroll = ""
        searchroll = self.textEdit_7.toPlainText()
        try:
            conn = sqlite3.connect("library.db")
            c = conn.cursor()
            result = c.execute("SELECT * FROM books WHERE BOOKID=" + str(searchroll))
            row = result.fetchone()
            searchresult = str(row[0])
            self.textEdit.setText(searchresult)
            self.textEdit_2.setText(str(row[1]))
            self.textEdit_3.setText(str(row[2]))
            self.textEdit_4.setText(str(row[3]))
            self.textEdit_5.setText(str(row[4]))

            conn.close()
        except Exception:
            print("Could not find user from database")

    def updatebook(self,bookedit):
        conn = sqlite3.connect('library.db')
        c = conn.cursor()
        conn.execute(
            ''' UPDATE  books SET BOOKNAME=?, BOOKAUTHOR=?, BOOKPUBLISHER=?, BOOKPAGE=? WHERE BOOKID = ? ''',
            (self.textEdit_2.toPlainText(), self.textEdit_3.toPlainText(), self.textEdit_4.toPlainText(),
             self.textEdit_5.toPlainText(), self.textEdit.toPlainText()))
        #result = QMessageBox.warning(bookedit, 'Message', 'Updated User!')
        conn.commit()
        #bookedit.show()
        conn.close()

    def deletebook(self,bookedit):

        conn = sqlite3.connect('library.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM books WHERE BOOKID=? ", (self.textEdit.toPlainText()))
        result = QMessageBox.warning(bookedit, 'Message', 'Deleted User!')
        bookedit.show()
        conn.commit()
        conn.close()

    def addbook(self, bookedit):

        bookıd = self.textEdit.toPlainText()
        bookname = self.textEdit_2.toPlainText()
        bookauthor = self.textEdit_3.toPlainText()
        bookpublisher = self.textEdit_4.toPlainText()
        bookpage = self.textEdit_5.toPlainText()
        conn = sqlite3.connect('library.db')
        conn.execute(
            ''' INSERT INTO books (BOOKID,BOOKNAME, BOOKAUTHOR, BOOKPUBLISHER, BOOKPAGE) VALUES (?,?,?,?,?) ''',
            (bookıd, bookname, bookauthor, bookpublisher, bookpage))
        result = QMessageBox.warning(bookedit, 'Message', 'Added Book!')
        bookedit.show()

        conn.commit()

    def setupUi(self, bookedit):
        bookedit.setObjectName("bookedit")
        bookedit.resize(790, 647)
        bookedit.setMinimumSize(QtCore.QSize(790, 647))
        bookedit.setMaximumSize(QtCore.QSize(790, 16777215))
        bookedit.setStyleSheet("QWidget{\n"
"\n"
"\n"
"    background-image: url(ds.jpg);\n"
"}")
        self.label = QtWidgets.QLabel(bookedit)
        self.label.setGeometry(QtCore.QRect(50, 190, 101, 21))
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
        self.label_2.setGeometry(QtCore.QRect(60, 250, 101, 20))
        self.label_2.setStyleSheet("QLabel{\n"
"\n"
"background: beige;\n"
"\n"
" color: blue;\n"
"    font-size: 18px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(bookedit)
        self.label_3.setGeometry(QtCore.QRect(60, 360, 101, 20))
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
        self.label_4.setGeometry(QtCore.QRect(40, 300, 121, 20))
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
        self.label_5.setGeometry(QtCore.QRect(60, 130, 91, 20))
        self.label_5.setStyleSheet("QLabel{\n"
"\n"
"background: beige;\n"
"\n"
" color: blue;\n"
"    font-size: 18px;\n"
"\n"
"}")
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(bookedit)
        self.textEdit.setGeometry(QtCore.QRect(180, 130, 161, 31))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"background: white;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(bookedit)
        self.textEdit_2.setGeometry(QtCore.QRect(180, 180, 161, 31))
        self.textEdit_2.setStyleSheet("QTextEdit{\n"
"background: white;\n"
"}")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(bookedit)
        self.textEdit_3.setGeometry(QtCore.QRect(180, 240, 161, 31))
        self.textEdit_3.setStyleSheet("QTextEdit{\n"
"background: white;\n"
"}")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(bookedit)
        self.textEdit_4.setGeometry(QtCore.QRect(180, 300, 161, 31))
        self.textEdit_4.setStyleSheet("QTextEdit{\n"
"background: white;\n"
"}")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(bookedit)
        self.textEdit_5.setGeometry(QtCore.QRect(180, 360, 161, 31))
        self.textEdit_5.setStyleSheet("QTextEdit{\n"
"background: white;\n"
"}")
        self.textEdit_5.setObjectName("textEdit_5")
        self.pushButton = QtWidgets.QPushButton(bookedit)
        self.pushButton.setGeometry(QtCore.QRect(430, 50, 101, 41))
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
        self.textEdit_7.setGeometry(QtCore.QRect(540, 50, 161, 31))
        self.textEdit_7.setStyleSheet("QTextEdit{\n"
"background: white;\n"
"}")
        self.textEdit_7.setObjectName("textEdit_7")
        self.pushButton_2 = QtWidgets.QPushButton(bookedit)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 500, 101, 61))
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
        self.pushButton_3.setGeometry(QtCore.QRect(230, 500, 101, 61))
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
        self.pushButton_3.clicked.connect(lambda :self.deletebook(bookedit))
        self.pushButton_2.clicked.connect(lambda : self.addbook(bookedit))
        self.pushButton_4 = QtWidgets.QPushButton(bookedit)
        self.pushButton_4.clicked.connect(lambda :self.updatebook(bookedit))


        self.pushButton_4.setGeometry(QtCore.QRect(430, 500, 101, 61))
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
        self.pushButton_5.setGeometry(QtCore.QRect(290, 590, 191, 28))
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
        self.pushButton.clicked.connect(self.searchbook)

        self.pushButton_6 = QtWidgets.QPushButton(bookedit)
        self.pushButton_6.setGeometry(QtCore.QRect(620, 500, 101, 61))
        self.pushButton_6.clicked.connect(self.listbook)

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
        self.tableWidget = QtWidgets.QTableWidget(bookedit)
        self.tableWidget.setGeometry(QtCore.QRect(430, 130, 301, 291))
        self.tableWidget.setStyleSheet("background: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

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
        self.pushButton.setText(_translate("bookedit", "Search"))
        self.pushButton_2.setText(_translate("bookedit", "Add"))
        self.pushButton_3.setText(_translate("bookedit", "Delete"))
        self.pushButton_4.setText(_translate("bookedit", "Update"))
        self.pushButton_5.setText(_translate("bookedit", "Turn Back Main Page"))
        self.pushButton_6.setText(_translate("bookedit", "Display"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("useredit", "BOOKID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("useredit", "BOOKNAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("useredit", "BOOKAUTHOR"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("useredit", "BOOKPUBLISHER"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("useredit", "BOOKPAGE"))



#import lili_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bookedit = QtWidgets.QWidget()
    ui = Ui_bookedit()
    ui.setupUi(bookedit)
    bookedit.show()
    sys.exit(app.exec_())
