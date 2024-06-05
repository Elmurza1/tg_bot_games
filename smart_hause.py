class Person:
    def __init__(self, name_pm, language_pm):
        self.name = name_pm
        self.language = language_pm
        self.money = []

    def introdice(self):
        if self.language == 'kg':
            print(f'салам! менин атым {self.name}')
        elif self.language == 'ru':
            print(f'привет! меня зовут {self.name}')
        else:
            print(f'hello!,my name is{self.name}')


class BankAccount(Person):
    def __init__(self, account_namar_pm, balance_pm ):
        self.namb = account_namar_pm
        self.balance = balance_pm


    def deposit(self, dep):
        self.money.append(dep)


    def list_money(self):
        return self.money


    def remove_money(self, rem_money):
        self.money.remove(rem_money)


peron = BankAccount(account_namar_pm=50, balance_pm=100000)

peron.deposit(122)
print(peron)









