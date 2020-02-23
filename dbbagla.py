import sqlite3

dbase = sqlite3.connect('library.db')

print('Database is opened')

"""dbase.execute(''' CREATE TABLE bookctg(
BOOKCATEGORYID INT PRIMARY KEY NOT NULL,
CATEGORYNAME TEXT NOT NULL)''')

dbase.execute(''' CREATE TABLE books(
BOOKID INT PRIMARY KEY NOT NULL,
BOOKNAME TEXT NOT NULL,
BOOKAUTHOR TEXT NOT NULL,
BOOKPUBLISHER TEXT NOT NULL,
BOOKPAGE INT NOT NULL,
FOREIGN KEY(USERID) REFERENCES user(USERID))''')




dbase.execute(''' CREATE TABLE user(
USERID INT PRIMARY KEY NOT NULL,
USERNAME TEXT NOT NULL,
USERSURNAME TEXT NOT NULL,
PHONENUMBER CHAR(11) NOT NULL,
USERLOGINNAME VARCHAR(15) NOT NULL,
PASSWORD INT NOT NULL,
BOOKID INT
''')


dbase.execute(''' CREATE TABLE admin(
ADMINID INT PRIMARY KEY NOT NULL,
ADMINUSERNAME VARCHAR(15) NOT NULL,
ADMINPASS INT NOT NULL)  
''')


dbase.execute(''' CREATE TABLE borrow(  #borrow 
ISSUEID INT PRIMARY KEY NOT NULL,
USERID INT NOT NULL,
BOOKID INT NOT NULL,
ISSUEDATE VARCHAR(50) NOT NULL,
RETURNDATE VARCHAR(50) NOT NULL,
BORROW INT NOT NULL,
FOREIGN KEY(USERID) REFERENCES user(USERID),
FOREIGN KEY(BOOKID) REFERENCES books(BOOKID))
''')


"""

#dbase.execute("""INSERT INTO books VALUES(?,?,?,?,?,?,?,?) """,('1','Rüzgarın Adı','Jack', 'Pegasus', '450','1','','') )

dbase.execute(''' INSERT INTO user VALUES(?,?,?,?,?,?,?)''',('2','Elif','Yilmaz', '05340330927','elifyilmaz','123456','3'))
#dbase.commit()

#dbase.execute(""" INSERT INTO admin VALUES(?,?,?)""", ('1','elif','12305'))
#dbase.commit()


#dbase.execute(""" ALTER TABLE user ADD BOOKID int  """)

#dbase.execute(""" ALTER TABLE user ADD BOOKNAME varchar(30)  """)
#dbase.execute("""ALTER TABLE books ADD BORROWUSERID int """)
#dbase.execute(""" ALTER TABLE books ADD BORROWUSERNAME varchar(30)  """)

#dbase.execute(""" DROP TABLE user """)

#dbase.execute("""INSERT INTO books VALUES(?,?,?,?,?,?,?) """,('1','Rüzgarın Adı','Jack', 'Pegasus', '450','','') )
#dbase.execute("""INSERT INTO issuereturn VALUES(?,?,?,?,?,?) """,('1','5','9', '8','','') )

#dbase.execute(''' ALTER TABLE issuereturn RENAME TO borrow''')












dbase.commit()

dbase.close()