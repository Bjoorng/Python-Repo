# The array type can hold homogeneous data types and operate
# on them more efficiently while using less memory

from array import array

# TODO: Create an array of integer numbers
arr1 = array('i', [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

# TODO: Add additional items to the array
# arr1.insert(5, 2)
# arr1.append(5)
# arr1.extend([24, 33, 56])
# print(arr1)

# TODO: iterate over the array content like any other list
# for i, element in enumerate(arr1):
#     arr1[i] = element*2
# print(arr1)

# TODO: Try to add a non-integer number to the array
# arr1.insert(0, 1.5) - this gives out an error since the added value is not an integer

# TODO: Create an array to hold bytes instead of ints
arr2 = array('B', [18, 102, 182, 56, 89, 5, 254, 32, 64, 50])

# TODO: try to add an item that's out of range
# arr2.append(480)

# TODO: Convert an array to a list
list1 = arr2.tolist()