import os
import fnmatch


def find_albums(root, artist_name):
    for path, directories, _ in os.walk(root):
        for artist in fnmatch.filter(directories, artist_name):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):
            yield song


if __name__ == "__main__":
    album_list = find_albums("music", "Aerosmith")
    song_list = find_songs(album_list)

    for s in song_list:
        print(s)
