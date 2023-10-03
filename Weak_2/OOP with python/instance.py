# program to know instance ans class attribute

class Shop():
    item_list1 = [] #This is class attribute which will apply every time
    def __init__(self, name):
        self.name = name
        self.list2 = [] # This is instance attribute which will apply just only for separate object

    def buy(self, item):
        self.item_list1.append(item)
        self.list2.append(item)


a = Shop("Morsalin")
a.buy("Sunglass")
a.buy("Watch")
a.buy("Pant")
a.buy("Shirt")

b = Shop("Morsalin")
b.buy("Sunglass")
b.buy("Watch")
b.buy("Pant")
b.buy("Shirt")


print(a.item_list1)
print("New Line")
print(a.list2)
