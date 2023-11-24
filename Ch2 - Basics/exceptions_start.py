#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

# Errors can happen in programs, and we need a clean way to handle them
# TODO: This code will cause an error because you can't divide by zero:

# x = 10/0


# TODO: Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
# try:
#     x = 10/0
# except:
#     print("not a valid division")

# TODO: You can also catch specific exceptions

result = None

try:
    answer = input("give me a number i should divide 10 by")
    number = int(answer)
    result = 10/number
    print("Here's the result", result)

except ValueError as e:
    print("You need to give me a number")
    print(e)
except ZeroDivisionError as e:
    print("You can't divide by zero")
finally:
    if result:
        print("Everything worked fine!")
    else:
        print("Something went wrong")
