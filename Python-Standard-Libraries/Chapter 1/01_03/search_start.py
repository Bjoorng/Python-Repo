# Use standard library functions to search strings for content


sampleStr = "The quick brown fox jumps over the lazy dog"

# TODO: startsWith and endsWith functions
print(sampleStr.startswith("The")) #the function is case sensitive so let's be careful when writing code
print(sampleStr.startswith("quick"))


# TODO: the find and rfind functions
print(sampleStr.find("quick")) #starts looking from the left and prints out the position
print(sampleStr.rfind("quick")) #starts looking from the right and prints out the position
print("quick" in sampleStr) #just gives true or false if the string includes the word or not

# TODO: using replace
newStr = sampleStr.replace("quick", "slow")
print(newStr)

# TODO: counting instances of substrings
result = int(sampleStr.count("over"))
print("the word you were looking for was used this many times:", result)
