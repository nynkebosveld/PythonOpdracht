__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import glob
import os
from zipfile import ZipFile
import shutil

# Public variables
my_zip_files = os.path.join(os.getcwd(), "data.zip")
my_cache_dir = os.path.join(os.getcwd(), "cache")


# Make a clean cache directory
def clean_cache():
    # Parent Directory path
    parent_dir = os.getcwd()

    # Path
    path = os.path.join(parent_dir, my_cache_dir)

    if os.path.exists(path):
        shutil.rmtree(path)
        os.mkdir(path)
    else:
        os.mkdir(path)


# Get all the files from the zip file
def cache_zip(my_zip_file, my_cache_directory):
    clean_cache()
    zip = ZipFile(my_zip_file, 'r')
    zip.extractall(my_cache_directory)


# Return a list of all files in the cache directory
def cached_files():
    filePattern = os.path.join(my_cache_dir, "*")
    return glob.glob(filePattern)


# Find the password
def find_password(files):
    keyword = 'password'

    # opening a text file
    for file in files:
        with open(file) as f:
            if keyword in f.read():
                f = open(file, "r")

                for line in f:
                    if keyword in line:
                        f.close()
                        return line[line.find(" ") + 1:-1]

if __name__ == "__main__":
    cache_zip(my_zip_files, my_cache_dir)
    print(find_password(cached_files()))
