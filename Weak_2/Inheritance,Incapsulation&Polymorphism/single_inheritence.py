#Base class or parent class attributes are uses in all child classes
# derived class or child class use parent class attribute
 # This program is a example of simple inheritance  also this is a single inheritance
class Gadget:
    def  __init__(self, brand, price, color, origin):
        self.brand  = brand
        self.price = price
        self.color = color
        self.origin = origin
    def run(self):
        return f"Running {self.brand}"


class Laptop:
    def __init__(self,memory, SSD, brand, price, color, origin):
        self.memory = memory

        super().__init__(brand,price, color, origin)
        

class Phone(Gadget):
    def __init__(self, dual_sim, brand, price, color, origin):
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)
    
    def __repr__(self) -> str:
        return f"dual_sim : {self.dual_sim} brand: {self.brand}  price : {self.price}   color : {self.color}  origin : {self.origin}"


    

class Camera(Gadget):
    def __init__(self, brand, price, color, origin, pixel):
        self.pixel = pixel
        super().__init__(brand, price, color, origin)
    
    def __repr__(self) -> str:
        return f"brand: {self.brand}  price : {self.price}  color: {self.color} origin : {self.origin}  pixel: {self.pixel}"

        
my_phone = Phone(True, "Samsung", 50000, "Black", "China")
print(my_phone)

my_camera = Camera("Samsung", 40000, 'Black', 'Bangladesh', "10 Mpx")
print(my_camera)

