#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def functionOne():
    print("This Is A Function In Python")


# TODO: function that takes arguments
def functionTwo(arg1, arg2):
    print(arg1, " ", arg2)

# TODO: function that returns a value
def functionThree(x):
    return x**3

# TODO: function with default value for an argument
def functionFour(arg1, arg2=2):
    result = 1
    for i in range(arg2):
        result = result * arg1
    return result

# TODO: function with variable number of arguments
def functionFive(*args):
    result = 0
    for x in args:
        result = result + x
    return result

# functionOne()
# print(functionOne()) #this doesn't print any value since the function has no return value
# print(functionOne) #this prints out the value of the function itself since the function hasn't been called with the parentheses

# functionTwo(10, 20)
# print(functionTwo(10, 20))
# print(functionThree(5))

# print (functionFour(3))
# print (functionFour(4, 3))
# print (functionFour(arg2=3, arg1=4))

print (functionFive(5, 7, 1))
print (functionFive(2, 5, 2 , 1 , 2, 5, 6))