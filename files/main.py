__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import glob
import os
from zipfile import ZipFile


def clean_cache():
    # Directory
    directory = "cache"

    # Parent Directory path
    parent_dir = "../pythonProject/"

    # Path
    path = os.path.join(parent_dir, directory)

    try:
        os.mkdir(path)
        print("Directory '% s' created" % directory)
    except OSError as e:
        for f in os.listdir(path):
            os.remove(os.path.join(path, f))


def cache_zip():
    clean_cache()
    zip = ZipFile("./data.zip", 'r')
    zip.extractall("./cache")


def cached_files():
    return glob.glob("./cache/*")


def find_password(files):
    keyword = 'password'

    # opening a text file
    for file in files:
        with open(file) as f:
            if keyword in f.read():

                f = open(file, "r")

                for line in f:
                    if keyword in line:
                        print(line)

    return f.close()

files = cached_files()
find_password(files)