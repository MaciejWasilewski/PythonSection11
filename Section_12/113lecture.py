import datetime
import pytz


class Account:
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Account {0} created with {1} balance.".format(self.name, str(self.balance)))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), -amount))

    def show_balance(self):
        print("Balance for {0} is {1}.".format(self.name, str(self.balance)))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                trans_type = "deposited"
            elif amount < 0:
                trans_type = "withdrawn"
                amount *= -1
            else:
                trans_type = "none"
            print("{0:6} {1} on {2} at {3} UTC, ({4} local)".format(amount, trans_type, self.name,
                                                                    date.strftime("%Y %B %d %H-%M-%S"),
                                                                    date.astimezone().strftime("%Y %B %d %H-%M-%S")))


if __name__ == "__main__":
    tim = Account("Tim", 0)
    # tim.show_balance()

    tim.deposit(1000)
    # tim.show_balance()
    tim.withdraw(500)
    tim.show_transactions()
    # tim.show_balance()
