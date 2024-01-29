# Basic file operations in Python


# TODO: open a file for writing data
# "w" means write, "r" means read, "a" means append, "r+" means read and write
newFile = open("newText.txt", "w")
newFile.write("First basic python file interaction test\n")
newFile.close()

# TODO: read a file's data
with open("newText.txt", "r") as newFile:
    text = newFile.read()
    print(text)

# TODO: Add data to an existing file
with open("newText.txt", "+a") as adding:
    adding.write("New line for the text file\n")
    adding.write("Second addition to the text file\n")
    adding.seek(0)
    text = adding.read()
    print(text)