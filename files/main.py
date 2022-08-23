__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import glob
import os
from zipfile import ZipFile

my_zip_file = os.path.join(os.getcwd(), "data.zip")
my_cache_dir = os.path.join(os.getcwd(), "cache")

def clean_cache():
    # Directory
    directory = "cache"

    # Parent Directory path
    parent_dir = my_cache_dir

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
    zip = my_zip_file
    zip.extractall("./cache")


def cached_files():
    filePattern = os.path.join(my_cache_dir, "*")
    globbed = glob.glob(filePattern)
    return  globbed


def find_password(files):
    keyword = 'password'

    # opening a text file
    for file in files:
        with open(file) as f:
            if keyword in f.read():

                f = open(file, "r")

                for line in f:
                    if keyword in line:
                        print(line[line.find(" ")+1:-1])

    return f.close()

files = cached_files()
find_password(files)