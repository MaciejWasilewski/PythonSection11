import id3reader_p3 as id3reader
import os
import re


def return_path(start: str, ext: str):
    for path, _, files in os.walk(start, topdown=True):
        for file in files:
            if re.search(r'.{0}\b'.format(ext), file):
                yield os.path.join(os.path.abspath(path), file)


if __name__ == "__main__":
    extension = 'emp3'
    root = 'music'
    error_list=[]
    for fname in return_path(root, extension):
        print(fname)
        try:
            id3r = id3reader.Reader(fname)
        except:
            error_list.append(fname)

    print(len(error_list))