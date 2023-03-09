import unittest

from enemy import Enemy, Troll
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

class EnemyTest(unittest.TestCase):
	def setUp(self) -> None:
		self.enemy = Enemy()
		self.enemy_knight = Enemy("Knight", 10, 100)

	def test_enemy_have_neme_when_name_is_not_set(self):
		self.assertEqual(self.enemy.name, "Enemy")

	def test_enemy_have_name_when_name_is_set(self):
		self.assertEqual(self.enemy_knight.name, "Knight")

	def test_enemy_have_hitpoints_when_hitpoints_are_not_set(self):
		self.assertEqual(self.enemy.hit_points, 0)

	def test_enemy_have_hitpoints_when_hitpoints_are_set(self):
		self.assertEqual(self.enemy_knight.hit_points, 10)

	def test_enemy_lives_when_lives_are_not_set(self):
		self.assertEqual(self.enemy.lives, 1)

	def test_enemy_lives_when_lives_are_set(self):
		self.assertEqual(self.enemy_knight.lives, 100)

	def test_enemy_is_damaged(self):
		self.enemy_knight.take_damage(11)
		self.assertLess(self.enemy_knight.lives, 100)


class TestTroll(unittest.TestCase):
	def setUp(self) -> None:
		self.enemy = Troll()
		self.ugly_enemy = Troll("Ugly_troll", 18, 3)

	def test_troll_have_neme_when_name_is_not_set(self):
		self.assertEqual(self.enemy.name, "Enemy")

	def test_troll_have_name_when_name_is_set(self):
		self.assertEqual(self.ugly_enemy.name, "Ugly_troll")

	def test_troll_have_hitpoints_when_hitpoints_are_not_set(self):
		self.assertEqual(self.enemy.hit_points, 0)

	def test_troll_have_hitpoints_when_hitpoints_are_set(self):
		self.assertEqual(self.ugly_enemy.hit_points, 18)

	def test_troll_lives_when_lives_are_not_set(self):
		self.assertEqual(self.enemy.lives, 1)

	def test_troll_lives_when_lives_are_set(self):
		self.assertEqual(self.ugly_enemy.lives, 3)

	def test_enemy_is_damaged(self):
		self.ugly_enemy.take_damage(20)
		self.assertLess(self.ugly_enemy.lives, 3)
