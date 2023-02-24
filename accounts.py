class Account:
	"""Simple class"""
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance

	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			self.show_balance()
		else:
			print(f"You can't deposit negative amount")

	def withdraw(self, amount):
		if 0 < amount <= self.balance:
			self.balance -= amount
			self.show_balance()
		else:
			print(f"Your amount have to be greater than 0 you can withdraw maximum {self.balance}")

	def show_balance(self):
		print("Balance is {}".format(self.balance))


"""Pomocí příkazu „if main“ můžete definovat kód, který bude spuštěn pouze,
když je modul spuštěn jako samostatný program, zatímco jakýkoli kód mimo tento blok bude spuštěn,
ať už je modul spuštěn jako samostatný program nebo importován do jiný program."""

if __name__ == "__main__":
	tim = Account("Tim", 0)
	tim.deposit(1000)
	tim.withdraw(500)
	tim.deposit(5000)
	tim.withdraw(10000)
