#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    print(os.name)
    
    # Check for item existence and type
    #print("here's the item you're looking for:", str(path.exists('textfile.txt')))
    #print("the item is a file:", path.isfile('textfile.txt'))
    #print("the item is a directory:", path.isdir('textfile.txt'))

    # Work with file paths
    #print("item's path:", path.realpath('textfile.txt'))
    #print("item's path and name:", path.split(path.realpath('textfile.txt')))
    
    # Get the modification time
    t = time.ctime(path.getmtime('textfile.txt'))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime('textfile.txt')))

    # Calculate how long ago the item was modified
    now = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime('textfile.txt'))
    print("the file was modified ", now, " moments ago")
    print("or: ", now.total_seconds(), "seconds ago")

if __name__ == "__main__":
    main()
