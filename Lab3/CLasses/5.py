class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposited ", amount, ".", " New balance: ", self.balance)
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdrawn", amount, ".", " New balance: ", self.balance)