import unittest
from main import Kettle, Turtle


class TestKonviceFunction(unittest.TestCase):
	def setUp(self) -> None:
		self.milk = Kettle("milk", 8.99)

	def test_price_of_milk(self):
		self.assertEqual(self.milk.price, 8.99)

	def test_name_of_milk(self):
		self.assertEqual(self.milk.make, "milk")

	def test_switch_to_on(self):
		self.milk.switch_to_on()
		self.assertTrue(self.milk.on)

	def test_power_source_of_konvice(self):
		self.assertEqual(self.milk.power_source, "electricity")


class TestTurtleFunction(unittest.TestCase):
	def setUp(self) -> None:
		self.turtle = Turtle("Tim", "green", 8, 9.99)

	def test_name_of_turtle(self):
		self.assertEqual(self.turtle.name, "Tim")

	def test_color_of_turtle(self):
		self.assertEqual(self.turtle.color, "green")

	def test_turtle_is_turbo(self):
		self.assertFalse(self.turtle.turbo, False)

	def test_turtle_size(self):
		self.assertEqual(self.turtle.size, 8)

	def test_turtle_price(self):
		self.assertEqual(self.turtle.price, 9.99)

	def test_turtle_turbo_on(self):
		self.turtle.turbo_on()
		self.assertTrue(self.turtle.turbo, True)

	def test_atribute_food_of_turtle(self):
		self.assertEqual(self.turtle.food, "omnivore")

# testing branch
