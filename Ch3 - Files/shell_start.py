#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    # make a duplicate of an existing file
    if path.exists("textfile.txt.bak"):
        # get the path to the file in the current directory
        src = path.realpath("textfile.txt")

        # let's make a backup copy by appending "bak" to the name
        # destination = src + ".bak"
        # shutil.copy(src, destination)

        # rename the original file
        # os.rename("textfile.txt", "renamedfile.txt")

        # now put things into a ZIP archive
        # root_dir, tail = path.split(src)
        # shutil.make_archive("zipped", "zip", root_dir)

        # more fine-grained control over ZIP files
        with ZipFile("newzip.zip", "w") as newzip:
            newzip.write("renamedfile.txt")
            newzip.write("textfile.txt.bak")

if __name__ == "__main__":
    main()
