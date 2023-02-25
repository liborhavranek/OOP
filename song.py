class Song:
	"""Class to represent a song
	Attributes:
	title: str, The title of the song
	artist: Artist, Object representing a creator
	duration: int, The duration of song in seconds
	"""

	def __init__(self, title, artist, duration=0):
		"""
		:param title: The title of the song
		:param artist: Artist, Object representing a creator
		:param duration: The duration of song in seconds, default is zero
		"""

		self.title = title
		self.artist = artist
		self.duration = duration


"""Show me documentation for everything in class"""
print("Documentation for everything in class")
help(Song)
print(80 * "-")

"""Show documentation for Init method in the class"""
print("documentation for init method in class")
help(Song.__init__)
print(80 * "-")

"""Show documentation for class"""
print("show documentation for class")
print(Song.__doc__)
print(80 * "-")

"""Show documentation for init in class """
print("show documentation for init in class")
print(Song.__init__.__doc__)

Song.__init__.__doc__ = """This is added init doc"""
help(Song.__init__)


class Album:
	"""Class represent an Album with tracklist
	Attributes:
	album_name (str): The name of the album.
	year (int): The year was album was released.
	artist: (Artist): The artist responsible for the album. If not specified,
	the artist will default to an artist with the name "Various Artists".
	tracks (List[Song]):  A list of the songs on the album.

	Methods:
		add_song: Used to add a new song to the album's track list.
	"""

	def __init__(self, name, year, artist=None):
		self.name = name
		self.year = year
		if artist is None:
			self.artist = Artist("various artist")
		else:
			self.artist = artist

		self.tracks = []

	def add_song(self, song, position=None):
		"""Add song to the tracklist
		Arguments:
		song (Song): A song to add.
		position (Optional[int]): If specified, the song will be added to that position
		in the track list - inserting it between other songs if necessary.
		Otherwise, the song will be added to the end of the list.
		"""
		if position is None:
			self.tracks.append(song)
		else:
			self.tracks.insert(position, song)


class Artist:
	"""Basic class to store artist data
	Attributes:
	name (str): The name of the artist.
		albums (List[Album]): A list of the albums by this artist.
		The list includes only those albums in this collection, it is
		not an exhaustive list of the artist's published albums.

	Methods:
	add_album: Use to add a new album to the artist's albums list
	"""

	def __init__(self, name):
		self.name = name
		self.albums = []

	def add_album(self, album):
		"""Add a new album to the list.

		Args:
		album (Album): Album object to add to the list.
		If the album is already present, it will not added again (although this is yet to implemented).
		"""
		self.albums.append(album)


def load_data():
	new_artist = None
	new_album = None
	artist_list = []

	with open("albums.txt", "r") as albums:
		for line in albums:
			# data row should consist of (artist, album, year, song)
			artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
			year_field = int(year_field)
			print("Artist: {}\t Album: {}\t Year: {}\t Song: {}\t".format(artist_field, album_field, year_field, song_field))

			if new_artist is None:
				new_artist = Artist(artist_field)
			elif new_artist.name != artist_field:
				new_artist.add_album(new_album)
				artist_list.append(new_artist)
				new_artist = Artist(artist_field)
				new_album = None

			if new_album is None:
				new_album = Album(album_field, year_field, new_artist)
			elif new_album.name != album_field:
				new_artist.add_album(new_album)
				new_album = Album(album_field, year_field, new_artist)

			new_song = Song(song_field, new_artist, 999)
			new_album.add_song(new_song)

		if new_artist is not None:
			if new_album is not None:
				new_artist.add_album(new_album)
			artist_list.append(new_artist)

	return artist_list


def create_checkfile(artist_list):
	"""Create a check file from the object data for comparison with the original file"""
	with open("checkfile.txt", 'w') as checkfile:
		for new_artist in artist_list:
			for new_album in new_artist.albums:
				for new_song in new_album.tracks:
					print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song), file=checkfile)


if __name__ == "__main__":
	artists = load_data()
	print("There are {} aritsts".format(len(artists)))
	create_checkfile(artists)
