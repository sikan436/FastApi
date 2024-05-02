def add(n1: int, n2: int):
    return n1+n2


class BankAccount():
    def __init__(self,starting_balance=0):
        self.balance=starting_balance

    def deposit(self,amount):
        self.balance=self.balance+amount

    def self_withdraw(self,amount):
        self.balance=self.balance-amount

    def collect_intrest(self):
        self.balance*=1.1