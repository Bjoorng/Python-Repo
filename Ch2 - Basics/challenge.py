#Challenge: write a program to check if the inputted text is palindrome

isRunning = True

def palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

while (isRunning):
    text = input("Insert text to check if the program works or exit to quit: ")
    
    if text == "exit":
        isRunning = False
        break

    text = text.lower()

    converted = ""
    for i in text:
        if i.isalnum():
            converted += i

    print("The test outcome is: ", palindrome(converted))