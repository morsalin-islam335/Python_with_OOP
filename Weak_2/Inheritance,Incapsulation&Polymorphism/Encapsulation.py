#program objective is to know about Encapsulation
class Bank:
    def __init__(self, holder_name, balance):
        self.name = holder_name
        self.__balance = balance # To do private data  we must use __(double underscore)

    def get_balance(self, amount):
        if(amount <= self.__balance):
            self.__balance -= amount
            return amount
        else:
            return f'insufficient money'

    def deposit(self, amount):
        self.__balance += amount
    
Sonali_Bank = Bank("Hasim", 1000)

print(Sonali_Bank.get_balance(500))

Sonali_Bank.deposit(10000)
print(Sonali_Bank.get_balance(100))

# print(Sonali_Bank._Bank__balance)
