




import sqlite3


fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')



# Create the database "test2.db"
conn = sqlite3.connect("test2.db")

with conn:
    cur = conn.cursor()
    # Create table "tbl_files" and add column "fileName"
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect("test2.db")

# Iterate through the list of file names and insert each file ending in
# ".txt." to "col_fileName"
for item in fileList:
    if item.endswith(".txt"):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_fileName) VALUES (?)", (item,))
# Print the added file names
            print(item)
conn.close()


