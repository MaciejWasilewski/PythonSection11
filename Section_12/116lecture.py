class Song:
    """Class to represent a song
    
    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the songs creator
        duration (int) The duration of the song in seconds. May be zero.
        """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """
    Class to represent an Album, using its track list

    Attributes:
        album_name (str): The name of the album.
        year (int): The year of release.
        artist: (Artist): The artist responsible for album. If not specified, the artist will default to an artist with
        the name 'Various Artist'
        tracks (List[Song]): A list of the songs on the album.

    Methods:
        add_song: Used to add a new song to the album's tracklist.
    """

    def __init__(self, name, year, artist=None):
        self.album_name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list

        :param song: A song to add
        :param position: If specified, the song will be added to that position in the track list
        - inserting it between other songs if necessary.
        Otherwise, the song will be added to the end of the list
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """
    Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): A list of the albums by this artist. The list includes only those albums in this
        collection, it is not an exhaustive list of the artist's published albums.

    Methods:
        add_album: Use to add a new album to the artist's album list.
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """
        Add a new album to the list
        :param album: Album object to add to the list. If the album is already present, it will not be added again
        (although this is yet to implemented)
        """
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []
    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None
            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.album_name != album_field:
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)
    return artist_list


def create_checkfile(par_artist_list):
    with open("checkfile.txt", "w") as checkfile:
        for artist in par_artist_list:
            for album in artist.albums:
                for song in album.tracks:
                    print("{0.name}\t{1.album_name}\t{1.year}\t{2.title}".format(artist, album, song), file=checkfile)


if __name__ == "__main__":
    artist_list = load_data()
    for i in range(len(artist_list)):
        print("{0:2}. {1}".format(i + 1, artist_list[i].name))
        for j in range(len(artist_list[i].albums)):
            print("-" * 3 + "{0:2}. {1}".format(j + 1, artist_list[i].albums[j].album_name))
            for song in artist_list[i].albums[j].tracks:
                print("-" * 6 + song.title)
    print("There are {} artist".format(len(artist_list)))
    create_checkfile(artist_list)
