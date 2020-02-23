import sqlite3 as sqlite

connection = sqlite.connect('library.db')
connection.row_factory = sqlite.Row  # Enables accessing columns via names
database = connection.cursor()


def getLogin(userloginname, password):
    result = database.execute(''' SELECT * FROM user WHERE userloginname = ? AND password = ? ''',(userloginname, password)).fetchall()
    if(len(result) == 1):
        return result[0]
    return False

def getBook(userID):
    query = "SELECT BOOKID, RETURNDATE FROM borrow WHERE USERID = %d" % userID
    result = database.execute(query).fetchall()
    if(len(result) == 1):
        return result[0]
    return False

def username(userID):
    query = "SELECT USERNAME FROM user WHERE USERID=%d" % userID
    result = database.execute(query).fetchall()
    if len(result)==1:
        return result[0]
    return False