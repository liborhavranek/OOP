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


milk = Konvice("milk", 8.99)

print(milk.make)
print(milk.price)


class Turtle(object):
    def __init__(self, name, color, size, price):
        self.name = name
        self.color = color
        self.size = size
        self.male = True
        self.female = False
        self.price = price
