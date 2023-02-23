a = 12
b = 4

print(a + b)
# plus je add 
print(a.__add__(b))


class Konvice(object):
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_to_on(self):
        self.on = True


milk = Konvice("milk", 8.99)
coffee = Konvice("coffee", 1.99)

print(milk.make)
print(milk.price)


class Turtle(object):
    def __init__(self, name, color, size, price):
        self.name = name
        self.color = color
        self.size = size
        self.turbo = False
        self.price = price

    def turbo_on(self):
        self.turbo = True


print("Models: {} = {}\n {} = {}".format(milk.make, milk.price, coffee.make, coffee.price))
print("Models:{0.make} = {0.price} \n {1.make} = {1.price}". format(milk, coffee))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""


print(milk.on)
milk.switch_to_on()
print(milk.on)
