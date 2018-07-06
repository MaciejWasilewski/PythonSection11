import sqlite3
import datetime
import pytz
db = sqlite3.connect("accounts.sqlite")

cursor = db.cursor()
for row in cursor.execute(
        "SELECT * FROM history"):
    utc_time = row[0]
    tzone = row[3]
    print("{0}\t{1}".format(utc_time, tzone))
    date=datetime.datetime.strptime(utc_time[:-6]+tzone, '%Y-%m-%d %H:%M:%S.%f%Z')
    print(date)
    print(str(date.astimezone(date.tzinfo)))
    #print(row)

cursor.close()
db.close()