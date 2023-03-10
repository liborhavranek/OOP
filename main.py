a = 12
b = 4

print(a + b)
# plus je add 
print(a.__add__(b))


class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_to_on(self):
        self.on = True


milk = Kettle("milk", 8.99)
coffee = Kettle("coffee", 1.99)

print(milk.make)
print(milk.price)


class Turtle(object):

    food = "omnivore"

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

tim = Turtle("Tim", "green", 8, 9.99)
ben = Turtle("ben", "red", 6, 3.99)

tim.power = 1.5
ben.power = 2
print(tim.power)
print(ben.power)


"""I can rewrite attribute of class and now every kettle will have Atomic Power
I can set attribute for each object example milk will have gas power 
"""
Kettle.power_source = "atomic"
milk.power_source = "gas"
print(Kettle.power_source)
print(milk.power_source)
print(coffee.power_source)

print(Kettle.__dict__)
print(milk.__dict__)
"""Then running print(coffee.__dict__) will return a dictionary containing
 the attributes and values of the "coffee" instance"""
print(coffee.__dict__)

# testing branch
# create methods1 branch
