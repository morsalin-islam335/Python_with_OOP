class Company:
    def __init__(self, name):
        self.name = name
        self.route = []
        self.bus  = []
        self.manager = []
        self.driver = []
    
class Driver:
    def __init__(self, name, license, age, experience):
        self.name = name
        self.license = license
        self.age = age
        self.experience = experience

class Counter:
    def  __init__(self, name):
        self.name = name

        

class Passenger:
    def __init__(self, name,destination, balance):
        self.name = name 
        self.balance = balance
        self.destination = destination

