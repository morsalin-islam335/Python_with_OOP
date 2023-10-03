class Vehicle:
    def __init__(self, name, prize):
        self.name = name ; self.prize = prize
    

class Bus(Vehicle):
    def __init__(self, name, prize, seat):
        self.seat = seat
        super().__init__(name, prize)
    
    def __repr__(self) -> str:
        return f"name :{self.name}"


class Truck(Vehicle):
    def __init__(self, name, prize, weight):
        self.weight = weight
        super().__init__(name, prize)
    
    def __repr__(self) -> str:
        return super().__repr__()

class Pick_Up_Track(Truck):
    def __init__(self, name, prize, weight, vegetable):
        self.vegetable = vegetable
        super().__init__(name, prize, weight)

    def __repr__(self) -> str:
        return super().__repr__()

class Ac_Bus(Bus):
    def __init__(self, name, prize, temperature, seat):
        self.temperature = temperature
        super().__init__(name, prize, seat)

    def __repr__(self) -> str:
        print(f" total seat: {self.seat}, ticket_prize : {self.prize}")
        return super().__repr__()

green_line = Ac_Bus("Green_line", 2000, 10, 90)
print(green_line)
