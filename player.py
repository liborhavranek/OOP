class Player(object):

	def __init__(self, name):
		self.name = name
		self._lives = 3
		self._level = 1
		self._score = 0
		self._ammo = 0

	def _get_lives(self):
		return self._lives

	def _set_lives(self, lives):
		if lives >= 0:
			self._lives = lives
		else:
			print("Lives can't be negative")
			self._lives = 0

	def _get_level(self):
		return self._level

	def _set_level(self, level):
		if level > 0:
			delta = level - self._level
			self._score = delta * 1000
			self._level = level
		else:
			print("level can't be less than 1")

	lives = property(_get_lives, _set_lives)
	level = property(_get_level, _set_level)

	"""
	The @property decorator indicates that this method should be treated like an attribute rather than a method,
	so it can be accessed like player.score instead of player.score().
	"""

	@property
	def score(self):
		return self._score

	"""
	Dekorátor @score.setter definuje metodu setter, která umožňuje nastavení proměnné instance _score. 
	Když je atribut skóre nastaven na novou hodnotu, zavolá se metoda skóre s novou hodnotou jako argumentem. 
	Tato hodnota je pak uložena v proměnné instance _score. Celkově tato vlastnost umožňuje 
	přístup k atributu skóre a jeho úpravu způsobem, který působí jako běžný atribut
	"""

	@score.setter
	def score(self, score):
		self._score = score

	"""
	The __str__ method is a special method in Python classes that returns a string representation of the object. 
	In this case, it returns a formatted string that includes the player's name, number of lives, current level,
	and current score.
	"""

	@property
	def ammo(self):
		return self._ammo

	@ammo.setter
	def ammo(self, ammo):
		self._ammo = ammo

	def __str__(self):
		return "Name {0.name}, Lives {0.lives}, Level {0.level}, Score {0.score}, Ammo {0.ammo}".format(self)
