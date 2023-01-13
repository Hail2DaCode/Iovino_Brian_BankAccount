class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance = 0,):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)
    def deposit(self, amount, repeat = 1):
        self.balance += amount * repeat
        return self
    def withdraw(self, amount, repeat = 1):
        if self.balance >= amount:
            self.balance -= amount * repeat
        else:
            print("Insufficient funds: Charging a 5$ fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(self.balance)
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
    @classmethod
    def info_for_all_accounts(cls):
        for account in BankAccount.all_accounts:
            account.display_account_info()


account_1 = BankAccount(0.05, 1000)
account_2 = BankAccount(0.08, 2000)
# account_1.display_account_info()
# account_2.display_account_info()
account_1.deposit(500).deposit(200).deposit(100).withdraw(500).yield_interest().display_account_info()
account_2.deposit(250, 2).withdraw(200, 4).yield_interest().display_account_info()
BankAccount.info_for_all_accounts()