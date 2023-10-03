# objective of this program is know about python class constructor


class Phone:
    
    def __init__(self, brand, price, color):
        #this is a constructor
        self.brand = brand
        self.price = price
        self.color = color
        #self is like this keyword in C++

my_phone = Phone("I-Phone", 1500000, "cyan")
print(my_phone.brand)
