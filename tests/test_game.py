import unittest

from player import Player


class TestRunner:
	def run_all_tests(self):
		loader = unittest.TestLoader()
		tests = loader.discover(start_dir='.')
		runner = unittest.TextTestRunner(verbosity=2)
		runner.run(tests)


if __name__ == '__main__':
	runner = TestRunner()
	runner.run_all_tests()


class TestGameFunction(unittest.TestCase):
	def setUp(self) -> None:
		self.player = Player("Gamer")

	def test_player_have_name(self):
		self.assertEqual(self.player.name, "Gamer")

	def test_player_have_three_lives(self):
		self.assertEqual(self.player.lives, 3)

	def test_player_start_in_first_level(self):
		self.assertEqual(self.player._level, 1)

	def test_player_start_with_zero_point_in_score(self):
		self.assertEqual(self.player._score, 0)

	def test_player_lives_cannt_drop_below_zero(self):
		self.player.lives -= 10
		self.assertEqual(self.player.lives, 0)

	def test_player_score_when_next_level(self):
		self.player.level += 5
		self.assertEqual(self.player._score, 5000)

	def test_player_start_with_zero_ammo(self):
		self.assertEqual(self.player.ammo, 0)
