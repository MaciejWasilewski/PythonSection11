import os
import re

root = "music"

for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        fs = os.path.split(path)
        print(fs)
        s_split = os.path.split(fs[0])
        print(s_split)
        for f in files:
            print(f)
            song_details = re.split(r'(?: - |.emp3)', f)[0:2]
            print(song_details)
            input()
