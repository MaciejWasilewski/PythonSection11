import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("DROP TABLE contacts")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 64353453, 'tim@mail.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'b@b.com')")
cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
for row in cursor:
    print(row)
cursor.close()
db.commit()
db.close()
