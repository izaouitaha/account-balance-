class Account:
    def __init__(self, account_number, account_balance, account_holder):
        self.account_number = account_number
        self.account_balance = float(account_balance)
        self.account_holder = account_holder

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount

    def check_balance(self):
        return self.account_balance


my_account = Account("1", 1000, "Taha")

my_account.deposit(500)
my_account.withdraw(300)

print(my_account.check_balance())


account2 = Account("2", 200, "Ali")

account2.deposit(100)
account2.withdraw(50)

print(account2.check_balance())
