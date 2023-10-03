
class Bank():
    def __init__(self, balance):
        self.balance = balance
        self.minimum_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if(amount > 0):
            self.balance += amount
    
    def withdraw(self, amount):

        if amount < self.minimum_withdraw:
            print( f"You can't withdraw bellow {self.minimum_withdraw}")
        elif amount > self.max_withdraw:
            print(f"You can't withdraw more than {self.max_withdraw}")
        
        else:
            self.balance -= amount
            print(f"You withdraw {amount} TK. Your balance after withdraw is {self.get_balance()}")

        

IBBL = Bank(150000)
IBBL.withdraw(25)
IBBL.get_balance()
IBBL.deposit(10000)
IBBL.withdraw(1000)


IBBL.withdraw(5000000)
