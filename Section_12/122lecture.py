# from time import time as time


class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        duration (int) The duration of the song in seconds. May be zero.
        """

    def __init__(self, title, duration=0):
        self.title = title
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)


class Album:
    """
    Class to represent an Album, using its track list

    Attributes:
        album_name (str): The name of the album.
        year (int): The year of release.
        the name 'Various Artist'
        tracks (List[Song]): A list of the songs on the album.

    Methods:
        add_song: Used to add a new song to the album's tracklist.
    """

    def __init__(self, name, year):
        self.album_name = name
        self.year = year
        self.tracks = []

    def add_song(self, song_name, position=None):
        """Adds a song to the track list

        :param song_name: A song to add
        :param position: If specified, the song will be added to that position in the track list
        - inserting it between other songs if necessary.
        Otherwise, the song will be added to the end of the list
        """
        song=Song(song_name)
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

    def add_song(self, par_album_field, par_year_field, par_song_field):
        albums_names_list = [x.album_name for x in self.albums]
        if par_album_field not in albums_names_list:
            temp_album = Album(par_album_field, par_year_field)
            self.add_album(temp_album)
            # album_pos = len(par_artist_list[artist_pos].albums) - 1
        else:
            temp_album = self.albums[albums_names_list.index(par_album_field)]
        temp_album.add_song(par_song_field)


def load_data2():
    with open("albums.txt", "r") as albums:
        par_artist_list = []
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            artist_names_list = [x.name for x in par_artist_list]
            if artist_field not in artist_names_list:
                temp_artist = Artist(artist_field)
                par_artist_list.append(temp_artist)
                # artist_pos = len(par_artist_list) - 1
            else:
                temp_artist = par_artist_list[artist_names_list.index(artist_field)]
                # artist_pos =
            temp_artist.add_song(album_field, year_field, song_field)
            # albums_names_list = [x.album_name for x in temp_artist.albums]
            # if album_field not in albums_names_list:
            #     temp_album = Album(album_field, year_field, temp_artist)
            #     temp_artist.add_album(temp_album)
            #     # album_pos = len(par_artist_list[artist_pos].albums) - 1
            # else:
            #     temp_album = temp_artist.albums[albums_names_list.index(album_field)]
            #     # album_pos = albums_names_list.index(album_field)
            #
            # temp_album.add_song(Song(song_field, temp_album))
        return par_artist_list


def load_data():
    new_artist = None
    new_album = None
    par_artist_list = []
    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            # print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                new_artist.add_album(new_album)
                par_artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None
            if new_album is None:
                new_album = Album(album_field, year_field)
            elif new_album.album_name != album_field:
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field)

            new_song = Song(song_field)
            new_album.add_song(new_song)

        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            par_artist_list.append(new_artist)
    return par_artist_list


def create_checkfile(par_artist_list):
    with open("checkfile.txt", "w") as checkfile:
        for artist in par_artist_list:
            for album in artist.albums:
                for song in album.tracks:
                    print("{0.name}\t{1.album_name}\t{1.year}\t{2.title}".format(artist, album, song), file=checkfile)


if __name__ == "__main__":
    artist_list = load_data2()

    # start = time.time()

    # artist_list = load_data2()
    # print((time.time() - start) / 2000)
    # for i in range(len(artist_list)):
    #     print("{0:2}. {1}".format(i + 1, artist_list[i].name))
    #     for j in range(len(artist_list[i].albums)):
    #         print("-" * 4 + "{0:2}. {1}".format(j + 1, artist_list[i].albums[j].album_name))
    #         for k in range(len(artist_list[i].albums[j].tracks)):
    #             print("-" * 8 + "{0:2}. {1}".format(k + 1, artist_list[i].albums[j].tracks[k].title))
    print("There are {} artist".format(len(artist_list)))
    print(artist_list[2].name)
    print(artist_list[2].albums[1].tracks[1].name)
    create_checkfile(artist_list)
