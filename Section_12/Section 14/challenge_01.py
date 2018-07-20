import os
import re


def return_path(start: str, ext: str):
    for path, _, files in os.walk(start, topdown=True):
        for file in files:
            if re.search(r'.{0}\b'.format(ext), file):
                yield os.path.join(path, file)


if __name__=="__main__":
    extension='emp3'
    root='music'
    for fname in return_path(root, extension):
        print(fname)
