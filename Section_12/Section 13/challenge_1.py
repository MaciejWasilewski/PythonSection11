import sqlite3

db = sqlite3.connect("contacts.sqlite")
tables_cursor = db.cursor()
tables_cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
records_cursor = db.cursor()
for row in tables_cursor:
    table_name = row[0]
    print("Table name: {0}".format(table_name))
    records_cursor.execute("SELECT * FROM {0}".format(table_name))
    for row2 in records_cursor:
        print(row2)

    print("\n\n")
records_cursor.close()
tables_cursor.close()
db.close()