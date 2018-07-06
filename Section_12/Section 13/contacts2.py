import sqlite3

db = sqlite3.connect("contacts.sqlite")
new_email = "anotherupdate@update.com"
phone = (input("Please input phone number: "))
update_sql = "UPDATE contacts SET email = ? WHERE contacts.phone=?"
update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
update_cursor.connection.commit()
print("{} rows updated".format(update_cursor.rowcount))
update_cursor.close()
for row in db.execute("SELECT * FROM contacts"):
    print(row)

db.close()
