# This program objective is to know about operator overloading and method overriding

class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("Eat Meet, Fatty food, fast food")

    def exercise(self):
        return NotImplementedError #if we use exercise method from other parent class, we must override this function
    

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team 
        super().__init__(name, age, height, weight)

    def eat(self):
        print("Vegetable, moderate diet")

    def __add__(self, other):
        return self.age + other.age

    def __sub__(self, other):
        return self.height - other.height
    
    def __mul__(self, other):
        return self.weight * other.weight
    
    def __truediv__(self, other):
        return self.weight / other.weight

Tamim = Cricketer("Tamim", 30, 68, 70, "Bangladesh")

# print(Tamim.exercise()) #This will happen error. If we want to use this, we must override this method inside child class

Tamim.eat()  #
Sakib = Cricketer("Sakib", 35, 65,72, "Bangladesh")

print(Tamim + Sakib)
print(Tamim - Sakib)
print(Tamim * Sakib)
print(Tamim / Sakib)


    
