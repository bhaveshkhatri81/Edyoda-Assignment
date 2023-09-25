# Challenge 4: Implement a Banking Account

class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate



account1 = Account("Ashish", 5000)


savings_account1 = SavingsAccount("John", 10000, 3)

print(account1.title)  
print(account1.balance)  

print(savings_account1.title)  
print(savings_account1.balance)  
print(savings_account1.interestRate)  