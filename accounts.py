import datetime
import pytz


class Account:
	"""Simple class"""

	@staticmethod
	def _current_time():
		utc_time = datetime.datetime.utcnow()
		return pytz.utc.localize(utc_time)
	"""Statická metoda je metoda, která patří do třídy a nemá přístup ke stavu třídy nebo instance. 
	Je podobná běžné funkci, ale je definována uvnitř třídy. 
	Na rozdíl od metod instance statické metody nepracují s instancí třídy a nevyžadují parametr self. 
	Místo toho je lze zavolat na samotnou třídu."""

	def __init__(self, name, balance):
		self.name = name
		self.transaction_list = []
		self.balance = balance
		print(f"Account  created for {name}")

	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			self.show_balance()
			self.transaction_list.append((Account._current_time(), amount))
		else:
			print(f"You can't deposit negative amount")

	def withdraw(self, amount):
		if 0 < amount <= self.balance:
			self.balance -= amount
			self.transaction_list.append((Account._current_time(), - amount))
			self.show_balance()

		else:
			print(f"Your amount have to be greater than 0 you can withdraw maximum {self.balance}")

	def show_balance(self):
		print("Balance is {}".format(self.balance))

	def show_transactons(self):
		for date, amount in self.transaction_list:
			if amount > 0:
				transaction_type = "deposited"
			else:
				transaction_type = "withdraw"
				amount *= -1
			print("{:6} {} on {} (local time was {})".format(amount, transaction_type, date, date.astimezone()))


"""Pomocí příkazu „if main“ můžete definovat kód, který bude spuštěn pouze,
když je modul spuštěn jako samostatný program, zatímco jakýkoli kód mimo tento blok bude spuštěn,
ať už je modul spuštěn jako samostatný program nebo importován do jiný program."""

if __name__ == "__main__":
	tim = Account("Tim", 0)
	tim.deposit(1000)
	tim.withdraw(500)
	tim.deposit(5000)
	tim.withdraw(10000)
	tim.show_transactons()
