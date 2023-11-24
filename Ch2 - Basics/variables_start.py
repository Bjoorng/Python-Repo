# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring a variable works
myint = "cammello"
print (myint)
mylist = [0, 1, "two", 3.2, False, "samoiedo", 8, True]
print (mylist)

# to access a member of a sequence type, use []
print (mylist[4]) #to print the last item of the list
print (mytuple[0]) #to print the first item of the list

# use slices to get parts of a sequence
print (mylist[1:4]) #1 is the starting index of the list, 4 last index value (list's lenght)
print (mylist[0:5:3]) #0 is the starting index of the list, 5 last index value (list's lenght) and 3 is the step value
print (mylist[1:9:2]) #same as the second print but with different values

# you can use slices to reverse a sequence
print (mylist[::-1]) #reverse the sequence, the double colons mean default start and default end

# dictionaries are accessed via keys
print (mydict["one"])

# ERROR: variables of different types cannot be combined
print ("entra? " + str(6)) #the str function converts an int value into a string

# Global vs. local variables in functions
def function():
    global mystr #adding global instructs python to reassign the value of the preexisting mystr variable
    mystr = "def" #mystr in the function counts as a local variable while the mystr above is a global variable
    print (mystr)

function()
print (mystr)

del mystr #deletes the value of the indicated variable
print(mystr) #will give error since the value has been deleted