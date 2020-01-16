"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""
import math

a = [2, 4, 1, 7, 9, 6]
b = [1, 3, 5, 10, 12, 30, 2000, 1926, 51655, 999999]

# Output the second element: 4:
find_4 = a.index(4)
print(a[find_4:find_4 + 1])

# Output the second-to-last element: 9
print(a[len(a)-2:len(a)-1])

# Output the last three elements in the array: [7, 9, 6]
print(a[len(a)-3:])

# Output the two middle elements in the array: [1, 7]
# make fn to handle


def get_middle_of_list(list_name):
    middle_of_list = math.floor(len(list_name) / 2)
    if middle_of_list % 2 == 0:
        print(list_name[middle_of_list:middle_of_list + 1])
    else:
        print(list_name[middle_of_list - 1:middle_of_list + 1])


get_middle_of_list(a)
get_middle_of_list(b)

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[:len(a)-1])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[7:12])
