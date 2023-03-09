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
		self._name = name
		self._transaction_list = [(Account._current_time(), balance)]
		self.__balance = balance
		print(f"Account  created for {name}")

	"""V Pythonu se jedno podtržítko před názvem proměnné, metody nebo atributu používá k označení,
	že položka má být „soukromá“."""

	"""__balance označen jako soukromý se dvěma podtržítky na začátku. To způsobí, 
	že název atributu bude interpretem "změněn" na _Account__balance, což ztíží přístup zvenčí třídy. 
	Stále je však technicky možné získat přístup k atributu a v případě potřeby jej upravit."""

	def deposit(self, amount):
		if amount > 0:
			self.__balance += amount
			self.show_balance()
			self._transaction_list.append((Account._current_time(), amount))
		else:
			print(f"You can't deposit negative amount")

	def withdraw(self, amount):
		if 0 < amount <= self.__balance:
			self.__balance -= amount
			self._transaction_list.append((Account._current_time(), - amount))
			self.show_balance()

		else:
			print(f"Your amount have to be greater than 0 you can withdraw maximum {self.__balance}")

	def show_balance(self):
		print("Balance is {}".format(self.__balance))

	def show_transactons(self):
		for date, amount in self._transaction_list:
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

	jeannie = Account("Jeannie", 800)
	jeannie.__balance = 200
	jeannie.deposit(500)
	jeannie.deposit(300)
	jeannie.deposit(300)
	jeannie.withdraw(1000)
	jeannie.show_transactons()
	jeannie.show_balance()
	jeannie._Account__balance = 40
	jeannie.show_balance()

	print(tim.__dict__)
	print(jeannie.__dict__)
