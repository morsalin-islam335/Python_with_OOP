# This program objective is to know about abstraction

from abc import ABC, abstractmethod
class Life(ABC):
    def __init__(self, name):
        self.name = name 
    @abstractmethod
    def eat(self):
        print("can eat")
    @abstractmethod  # if we use this we can modify internal instance method
    def move(self):
        print("can move")

class Monkey(Life):
    def __init__(self, name):
        super().__init__(name)
        self.category = 'Monkey'

    def eat(self):
        print("Eat banana")
    def move(self):
        print("Can move")
class Tree(Life):
    def __init__(self, name):
        super().__init__(name)
        self.category = 'tree'
    
    def eat(self):
        print("drink but can't eat")
    def move(self):
        print("can't move")

monkey = Monkey("Tomy")
monkey.eat()

tree = Tree("Mango")
print(tree.name)





print(issubclass(Monkey, Life))
print(isinstance(monkey, Life))


   

    

