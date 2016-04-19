class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        self.balance -= amount

    def receive(self, amount):
        self.balance += amount

    def print_balance(self):
        print('Balance of:')
        print(self.name)
        print('is:')
        print(self.balance)

    def transfer(self, other, amount):
        self.pay(amount)
        other.receive(amount)


tojas = BankAccount('Tamas Kokeny', 46)
feri = BankAccount('Feri *', 7000000)
tojas.receive(130000)

tojas.transfer(feri, 40000)


tojas.print_balance()




