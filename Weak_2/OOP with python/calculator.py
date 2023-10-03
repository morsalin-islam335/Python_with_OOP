#program to create a simple calculator by using class

class Calculator():
    def add(self,x,y):
        return x + y
    def sub(self, x, y):
        return x - y
    def mul(self, x, y):
        return x * y
    def dev(self, x, y):
        return x // y

my_calculator = Calculator()

addition = my_calculator.add(10,5)
subtraction = my_calculator.sub(10,5)
multiplication = my_calculator.mul(10,5)
division = my_calculator.dev(10,5)

print(addition)
print(subtraction)
print(multiplication)
print(division)

