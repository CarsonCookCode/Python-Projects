Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sqlite3
>>> connection = sqlite3.connect("C:/Users/carso/Github_Repos/Python-Projects/myDatabase.db")
>>> peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
>>> 
>>> witth sqlite3.connect('myDatabase.db') as connection:
	
SyntaxError: invalid syntax
>>> with sqlite3.connect('myDatabase.db') as connection:
	c = connection.cursor()
	c.execute("DROP TABLE IF EXISTS People")
	c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
	c.executemany("INSERT INTO People VALUES(?, ?, ?)",
		      peopleValues)

	
<sqlite3.Cursor object at 0x0000015E297977A0>
<sqlite3.Cursor object at 0x0000015E297977A0>
<sqlite3.Cursor object at 0x0000015E297977A0>
>>> c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
<sqlite3.Cursor object at 0x0000015E297977A0>
>>> for row in c.fetchall()
SyntaxError: invalid syntax
>>> for row in c.fetchall():
	print (row)

	
('Ron', 'Obvious')
('Luigi', 'Vercotti')
>>> 
>>> c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
<sqlite3.Cursor object at 0x0000015E297977A0>
>>> while True:
	row = c.fetchone()
	if row = c.fetchone()
	
SyntaxError: invalid syntax
>>> while True:
	row = c.fetchone()
	if row is None:
		break
	print(row)

	
('Ron', 'Obvious')
('Luigi', 'Vercotti')
>>> 