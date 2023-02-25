import unittest

from accounts import Account
from main import Kettle, Turtle
from song import Song, Album, Artist


class TestRunner:
	def run_all_tests(self):
		loader = unittest.TestLoader()
		tests = loader.discover(start_dir='.')
		runner = unittest.TextTestRunner(verbosity=2)
		runner.run(tests)


if __name__ == '__main__':
	runner = TestRunner()
	runner.run_all_tests()


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
		self.assertEqual(self.milk.power_source, "atomic")


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
		self.assertGreater(self.tim._Account__balance, 0)

	def test_deposit_money_when_deposit_less_than_zero(self):
		"""Test testing if balance after deposited money is
		less than zero deposit will not add to account"""
		start_deposit = self.tim._Account__balance
		self.tim.deposit(-500)
		negative_deposit = self.tim._Account__balance
		self.assertEqual(start_deposit, negative_deposit)

	def test_withdraw_money_when_balance_is_grather_than_withdraw(self):
		"""Test testing if balance after withdraw money is
		less than balance before withdraw money"""
		self.tim.deposit(5000)
		balance_before_withdraw = self.tim._Account__balance
		self.tim.withdraw(4000)
		balance_after_withdraw = self.tim._Account__balance
		self.assertGreater(balance_before_withdraw, balance_after_withdraw)

	def test_withdraw_money_when_balance_is_less_than_withdraw(self):
		"""Test testing if balance is the same after withdraw money like
		before withdraw money because withdraw money what i haven't in account
		is not possible"""
		self.tim.deposit(5000)
		balance_before_withdraw = self.tim._Account__balance
		self.tim.withdraw(6000)
		balance_after_withdraw = self.tim._Account__balance
		self.assertEqual(balance_before_withdraw, balance_after_withdraw)

	def test_transaction_append_to_list_when_withdraw_money(self):
		"""Test testing if is in list all transaction"""
		self.tim.deposit(5000)
		self.tim.withdraw(1000)
		self.assertGreaterEqual(len(self.tim._transaction_list), 2)

	def test_transascton_append_to_list_when_deposti_money(self):
		"""Test testing if is in list all transaction"""
		self.tim.deposit(5000)
		self.tim.deposit(1000)
		self.assertGreaterEqual(len(self.tim._transaction_list), 2)

	def test_transaction_append_to_list_when_withdraw_money_greater_than_balance(self):
		"""Test testing if is in list all transaction"""
		self.tim.deposit(5000)
		self.tim.withdraw(6000)
		self.assertGreaterEqual(len(self.tim._transaction_list), 1)



class TestSong(unittest.TestCase):
	def setUp(self) -> None:
		self.song = Song("Time", "Hans Zimmer", 359)

	def test_song_have_title(self):
		self.assertEqual(self.song.title, "Time")

	def test_song_have_artist(self):
		self.assertEqual(self.song.artist, "Hans Zimmer")

	def test_song_have_duration(self):
		self.assertEqual(self.song.duration, 359)




class TestAlbum(unittest.TestCase):
	def setUp(self) -> None:
		self.album = Album("Pepek Mixtape", 1999, "pepek")

	def test_album_have_name(self):
		self.assertEqual(self.album.name, "Pepek Mixtape")

	def test_album_have_year(self):
		self.assertEqual(self.album.year, 1999)

	def test_album_have_artist_when_artist_is_none(self):
		self.none_album = Album("Pepek Mixtape", 1999)
		self.assertEqual(self.none_album.artist.name, "various artist")

	def test_album_have_artist_when_artist_is_defined(self):
		self.assertEqual(self.album.artist, "pepek")

	def test_new_song_is_added_in_the_list_when_position_is_none(self):
		new_song = Song("New Song", Artist("New Artist"), 180)
		self.album.add_song(new_song, None)
		self.assertIn(new_song, self.album.tracks)

	def test_new_song_is_added_in_the_list_when_position_is_defined(self):
		new_song = Song("New Song", Artist("New Artist"), 180)
		self.album.add_song(new_song, 1)
		self.assertIn(new_song, self.album.tracks)


class TestArtist(unittest.TestCase):
	def setUp(self) -> None:
		self.artist = Artist("Hans Zimmer")
		self.new_album = Album("New Album", 2023)

	def test_artist_have_name(self):
		self.assertEqual(self.artist.name, "Hans Zimmer")

	def test_add_new_album_in_album_list(self):
		self.artist.add_album(self.new_album)
		self.assertIn(self.new_album, self.artist.albums)

