import sqlite3
from tkinter import END

dbase = sqlite3.connect('library.db')


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from PyQt5 import QtCore, QtGui, QtWidgets


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_listofbook(object):

    def __init__(self, userID):
        self.userID = userID

    def searchbook(self):
        searchroll = ""
        searchroll = self.textEdit.toPlainText()
        try:
            conn = sqlite3.connect("library.db")
            c = conn.cursor()
            result = c.execute("SELECT * FROM books WHERE BOOKID= " + str(searchroll))
            row = result.fetchone()

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(row):  # enumerate ögelere sıra veriyor
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.connection.close()

                 # aradığım ID nin datalarını 6 kez yazdırıyor. Databasedeki column sayısı kadar bunu çöz.

            conn.close()

        except Exception:
            """result = QMessageBox.warning(listofbook, 'Message', 'Could not found that book in database!')
            listofbook.show()"""


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

    def setupUi(self, listofbook):
        listofbook.setObjectName("listofbook")
        listofbook.resize(582, 493)
        listofbook.setMinimumSize(QtCore.QSize(582, 493))
        listofbook.setMaximumSize(QtCore.QSize(582, 16777215))
        listofbook.setStyleSheet("QWidget{\n"
"background-image: url(yp.jpg);\n"
"}\n"
"")
        self.textEdit = QtWidgets.QTextEdit(listofbook)
        self.textEdit.setGeometry(QtCore.QRect(250, 43, 171, 31))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"\n"
"background:white;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(listofbook)
        self.pushButton.setGeometry(QtCore.QRect(100, 30, 121, 41))

        self.pushButton.clicked.connect(self.searchbook)
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
        self.pushButton_2.setGeometry(QtCore.QRect(190, 380, 191, 51))
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
        self.tableWidget = QtWidgets.QTableWidget(listofbook)
        self.tableWidget.setGeometry(QtCore.QRect(90, 160, 401, 192))
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


        self.pushButton_3 = QtWidgets.QPushButton(listofbook)
        self.pushButton_3.clicked.connect(self.listbook)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 110, 121, 41))
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

        self.retranslateUi(listofbook)
        QtCore.QMetaObject.connectSlotsByName(listofbook)

    def retranslateUi(self, listofbook):
        _translate = QtCore.QCoreApplication.translate
        listofbook.setWindowTitle(_translate("listofbook", "Book List"))
        self.pushButton.setText(_translate("listofbook", "Search"))
        self.pushButton_2.setText(_translate("listofbook", "Turn Back Main Page"))
        self.pushButton_3.setText(_translate("listofbook", "List Books"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("listofbook", "BOOKID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("listofbook", "BOOKNAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("listofbook", "BOOKAUTHOR"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("listofbook", "BOOKPUBLISHER"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("listofbook", "BOOKPAGE"))


#import ic_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    listofbook = QtWidgets.QWidget()
    ui = Ui_listofbook(listofbook)
    ui.setupUi(listofbook)
    listofbook.show()
    sys.exit(app.exec_())
