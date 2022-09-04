__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import glob
import os
from zipfile import ZipFile

my_zip_files = os.path.join(os.getcwd(), "data.zip")
my_cache_dir = os.path.join(os.getcwd(), "cache")


def clean_cache():
    # Parent Directory path
    parent_dir = os.path.pardir

    # Path
    path = os.path.join(parent_dir, my_cache_dir)

    if(os.path.exists(path)):
        for f in os.listdir(path):
            os.remove(os.path.join(path, f))
    else:
        for f in os.listdir(path):
            os.remove(os.path.join(path, f))

def cache_zip():
    clean_cache()
    zip = ZipFile(my_zip_files, 'r')
    zip.extractall(my_cache_dir)


def cached_files():
    filePattern = os.path.join(my_cache_dir, "*")
    return glob.glob(filePattern)


def find_password(files):
    keyword = 'password'

    # opening a text file
    for file in files:
        with open(file) as f:
            if keyword in f.read():
                f = open(file, "r")

                for line in f:
                    if keyword in line:
                        print(line[line.find(" ") + 1:-1])

    return f.close()


find_password(cached_files())