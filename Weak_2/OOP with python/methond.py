def call():
    print("calling done")

class Phone:
    brand  = "I-Phone"
    price = 150000
    color = 'Red'
    def call():
        print("2nd call")
        

my_phone = Phone()
print(my_phone.brand)
print(my_phone.color)
print(my_phone.price)

