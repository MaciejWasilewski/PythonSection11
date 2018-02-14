import datetime
import pytz


class Account:
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = []
        self._transaction_list.append((Account._current_time(), balance))
        print("Account {0} created with {1} balance.".format(self._name, str(self.__balance)))

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if amount > 0:
            self.__balance -= amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), -amount))

    def show_balance(self):
        print("Balance for {0} is {1}.".format(self._name, str(self.__balance)))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if not amount == 0:
                if amount > 0:
                    trans_type = "deposited"
                else:
                    trans_type = "withdrawn"
                    amount *= -1
                print("{0:6} {1} on {2} at {3} UTC, ({4} local)".format(amount, trans_type, self._name,
                                                                        date.strftime("%Y %B %d %H-%M-%S"),
                                                                        date.astimezone().strftime(
                                                                            "%Y %B %d %H-%M-%S")))


if __name__ == "__main__":
    tim = Account("Tim", 0)
    # tim.show_balance()
    steph = Account("Steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    tim.deposit(1000)
    # tim.show_balance()
    tim.withdraw(500)
    tim.__balance = 100
    tim.show_transactions()
    steph.show_transactions()
    # tim.show_balance()
