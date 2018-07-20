import sqlite3
import datetime
import pytz

db = sqlite3.connect("accounts.sqlite")
db.execute("CREATE table if not exists accounts (name text primary key not null, balance integer not null)")
db.execute(
    "CREATE TABLE IF NOT EXISTS history "
    "(time TIMESTAMP NOT NULL, account TEXT NOT NULL, amount INTEGER NOT NULL, tzone TEXT NOT NULL, "
    "PRIMARY KEY (time, account))")
# db.execute(
#  "CREATE VIEW IF NOT EXISTS localhistory AS SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') "
# "AS localtime, history.account, history.amount FROM history ORDER BY history.time")


class Account(object):

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow()), datetime.datetime.now(
            datetime.timezone.utc).astimezone().tzinfo

    def __init__(self, name: str, opening_balance: int = 0.0):
        cursor = db.cursor()
        cursor.execute("SELECT name, balance FROM accounts WHERE (name=?)", (name,))
        row = cursor.fetchone()
        if row:
            self.name, self._balance = row
            print("Retrieved record for {0}.".format(self.name))
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            cursor.close()
            print("Account created for {0}.".format(self.name))
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        cursor = db.cursor()
        deposit_time = self._current_time()
        try:
            cursor.execute("insert INTO history VALUES (?,?,?,?)", (deposit_time[0], self.name, amount, str(deposit_time[1])))
            cursor.execute("UPDATE accounts SET balance = ? WHERE (name=?)", (new_balance, self.name))
        except sqlite3.Error:
            cursor.connection.rollback()
        else:
            self._balance = new_balance
        finally:

            cursor.connection.commit()
            cursor.close()

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            self._save_update(amount)
            print("{0:.2f} deposited on {1} account.".format(amount / 100, self.name))
            self.show_balance()
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._save_update(-amount)
            print("{0:.2f} widthdrawn on {1} account.".format(amount / 100, self.name))
            self.show_balance()
            return amount / 100
        else:
            print("The amount has to be greater than zero and no more than account balance.")
            return 0.0

    def show_balance(self):
        print("Balance on account {0} is {1:.2f}".format(self.name, self._balance / 100))


if __name__ == "__main__":
    john = Account("John")
    john.deposit(10)
    john.deposit(60)
    john.withdraw(0)
    john.withdraw(60)
    john.show_balance()

    terry = Account("TerryJ")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)
    michael = Account("Michael")
