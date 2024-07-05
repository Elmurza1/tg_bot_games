class MBankAccount:
    def __init__(self, account_num_pm, balance_pm):
        self.account_num = account_num_pm
        self.__balance = balance_pm



    def get_balance(self):
        return self.__balance

    def set_balance(self, balance: int):
        if balance > 0:
            self.__balance = balance

    def deposit(self, none1):
        self.__balance += none1

    def withdraw(self, none):
        if 0 < none <= self.__balance:
            self.__balance -= none


account = MBankAccount(234, 12000)

print(account.get_balance())

account.deposit(5000)
print(account.get_balance())

account.withdraw(500)
print(account.get_balance())