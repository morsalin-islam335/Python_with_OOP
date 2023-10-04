# This program objective is to know about  static attribute, static method and class method

class Shoping_Mall:
    string = "Shoping Mall" # This is a static attribute
     
    def __init__(self, name) -> None:
        self.name = name # This is a instance attribute
        self.item = ['Pant', "Shirt"] # This is a instance attribute

class Shop(Shoping_Mall):
    def __init__(self, name) -> None:
        super().__init__(name)        

    def add_item(self, item):
        if item not in self.item:
            self.item.append(item)
    
    def show_item(self):
        print(self.item)
    
    @classmethod
    def show(self, item):
        print(item)
        print(self.string) #here is use instance attribute
    
    @staticmethod
    def add(x,y):
        print(x + y)




Boshundhora = Shop("Boshundhora")
Boshundhora.show_item()
Boshundhora.add(10,20)


Shop.show("Pant")
Shop.add(10,50)  #static method


    
