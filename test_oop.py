import unittest

from accounts import Account
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


class TestAccountFunction(unittest.TestCase):
	def setUp(self) -> None:
		self.tim = Account("Tim", 0)

	def test_deposit_money_when_deposit_grather_then_zero(self):
		"""Test testing if balance after deposited money is greater than zero"""
		self.tim.deposit(500)
		self.assertGreater(self.tim.balance, 0)

	def test_deposit_money_when_deposit_less_than_zero(self):
		"""Test testing if balance after deposited money is
		 less than zero deposit will not add to account"""
		start_deposit = self.tim.balance
		self.tim.deposit(-500)
		negative_deposit = self.tim.balance
		self.assertEqual(start_deposit, negative_deposit)

	def test_withdraw_money_when_balance_is_grather_than_withdraw(self):
		"""Test testing if balance after withdraw money is
		less than balance before withdraw money"""
		self.tim.deposit(5000)
		balance_before_withdraw = self.tim.balance
		self.tim.withdraw(4000)
		balance_after_withdraw = self.tim.balance
		self.assertGreater(balance_before_withdraw, balance_after_withdraw)

	def test_withdraw_money_when_balance_is_less_than_withdraw(self):
		"""Test testing if balance is the same after withdraw money like
		before withdraw money because withdraw money what i haven't in account
		is not possible"""
		self.tim.deposit(5000)
		balance_before_withdraw = self.tim.balance
		self.tim.withdraw(6000)
		balance_after_withdraw = self.tim.balance
		self.assertEqual(balance_before_withdraw, balance_after_withdraw)


