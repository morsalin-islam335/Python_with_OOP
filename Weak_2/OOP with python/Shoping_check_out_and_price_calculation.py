class Shoping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {"item": item, 'price': price, "quantity": quantity}

        self.cart.append(product)
    def check_out(self, amount):
        cost = 0
        for item in self.cart:
            cost += item['price'] * item["quantity"]
        if(amount < cost):
            print(f"please provide {cost - amount} TK more money")
        else:
            print(f"Your extra money is {amount - cost}")




Morsalin = Shoping("Morsalin")
Morsalin.add_to_cart("Rich", 50,50)
Morsalin.add_to_cart("Vegetable", 10, 50)

Morsalin.check_out(1000)