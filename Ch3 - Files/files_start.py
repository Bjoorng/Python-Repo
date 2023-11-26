#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():  
    # Open a file for writing and create it if it doesn't exist
    #file = open("textfile.txt", "w+")

    # Open the file for appending text to the end
    file = open("textfile.txt", "a+")

    # write some lines of data to the file
    # for i in range(10):
    #     file.write("testing the writing function\n")
    # for i in range(10):
    #     file.write("testing the append method\n")
    
    # close the file when done
    # file.close()
    
    # Open the file back up and read the contents
    file = open('textfile.txt', 'r')
    if file.mode == 'r':
        # First Method
        # contents = file.read() 
        # print(contents)

        # Second Method - This will read the contents of the file as an array/list and print them individually
        singleline = file.readline()
        for x in singleline:
            print(x)
    
if __name__ == "__main__":
    main()
