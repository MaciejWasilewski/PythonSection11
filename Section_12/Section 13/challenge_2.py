import sqlite3

db = sqlite3.connect("contacts.sqlite")
row_cursor = db.cursor()
name=input("Enter the name: ")

row_cursor.execute("SELECT * FROM contacts WHERE contacts.name LIKE ?", (name,))

for row in row_cursor:
    print(row)
row_cursor.close()
db.close()