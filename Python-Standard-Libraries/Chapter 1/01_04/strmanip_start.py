# Working with string manipulation functions

test_string1 = "The quick brown fox jumps over the lazy dog on the 1st of December"

# TODO: upper and lower convert between cases
print(test_string1.upper())
print(test_string1.lower())

# TODO: Use the split and join functions
splitted = test_string1.split(" ")
print(splitted)
nickelback = ["look", "at", "this", "photograph/", "every", "time", "i", "do", "it", "makes", "me", "laugh"]
print(" ".join(nickelback))

# TODO: use justification functions to align strings
# ljust, center, rjust
# just added the if statement to make it cleaner because of reasons
names = ["Amy", "John", "George", "Michael", "Penelope"]
biggest = max(len(name) for name in names)
for i in names:
    if i is biggest:
        print(i.ljust(biggest) + ":")
    else:
        print(i.ljust(biggest, "-") + ":")
for i in names:
    if i is biggest:
        print(i.center(biggest) + ":")
    else:
        print(i.center(biggest, "-") + ":")
for i in names:
    if i is biggest:
        print(i.rjust(biggest) + ":")
    else:
        print(i.rjust(biggest, "-") + ":")

# TODO: Use a translation table to replace characters
sample_str = "The quick brown fox jumped over the lazy dog"
trans_str = str.maketrans("abegilostz", "4636110572")
print(sample_str)
print(trans_str)