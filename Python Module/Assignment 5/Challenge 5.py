# Challenge 5: Handling a Bank Account

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Invalid withdrawal amount")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate) / 100


demo1 = SavingsAccount("Ashish", 2000, 5)

demo1.deposit(1000)
demo1.withdrawal(500)

print("Current Balance:", demo1.getBalance())

interest = demo1.interestAmount()
print("Interest Amount:", interest)
