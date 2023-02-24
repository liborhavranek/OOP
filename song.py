class Song:
	"""Class to represent a song
	Atributes:
	title: str, The title of the song
	artist: Artist, Object representing a creator
	duration: int, The duration of song in seconds
	"""

	def __init__(self, title, artist, duration):
		"""
		:param title: The title of the song
		:param artist: Artist, Object representing a creator
		:param duration: The duration of song in seconds, default is zero
		"""

		self.title = title
		self.artist = artist
		self.duration = duration
