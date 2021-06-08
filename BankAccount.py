class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        self.balance *= (1 + self.int_rate)
        return self
        
    @classmethod
    def all_account(cls):
        # we use cls to refer to the class
        for account in cls.all_accounts:
            print(f"Balance: ${account.balance}")

account1 = BankAccount(0.10, 100)
account2 = BankAccount(0.20, 1000)

account1.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()
account2.deposit(100).deposit(100).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

BankAccount.all_account()