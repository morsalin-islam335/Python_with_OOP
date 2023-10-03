class Laptop:
    def __init__(self, brand, price, memory):
        self.brand  = brand
        self.price = price
        self.memory = memory

    def run(self):
        return f"Running Laptop"
    
    def coding(self):
        return f"Learning Python and practicing"

class Phone:
    def __init__(self, brand, price, color, dual_sim):
        self.brand = brand
        self.price = price
        self.dual_sim = dual_sim

    def phone_call(self, number, text):
        return f"sending SMS {number} with {text}"
    def run(self):
        return f"Run Phone"
    
    