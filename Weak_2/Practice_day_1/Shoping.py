# The objective of this program is to know about inheritance, Encapsulation and polymorphism


class Product:
    def __init__(self):
        self.product = []
 
    
class Shop(Product):
    def __init__(self):
        super().__init__()
    
    def add_product(self, item):
        self.product.append(item)
    
    def product_list(self):
        print(self.product)

    def buy_product(self, item):
        if item in self.product:
            print("Congrats")
        else:
            print("Sorry. This item is currently unavailable")


my_shop = Shop()
my_shop.add_product("T-Shirt")
my_shop.add_product("Shirt")
my_shop.add_product("Pant")
my_shop.add_product("Panjabi")
my_shop.add_product("Bag")



my_shop.buy_product("Sar ani")
my_shop.buy_product("T-Shirt")
my_shop.buy_product("Pant")

my_shop.product_list()