#Write a program that writes the names of the files inside the folder and the bitcount of all the files

import os

total = 0

dirlist = os.listdir()
for i in dirlist:
    if os.path.isfile(i):
        size = os.path.getsize(i)
        total += size

os.mkdir("results")

resfile = open("results/res.txt", "w+")
if resfile.mode == "w":
    resfile.write("Bytecount: " + str(total) + "\n")
    resfile.write("List: \n")
    for i in dirlist:
        if os.path.isfile(i):
            resfile.write(i + "\n")