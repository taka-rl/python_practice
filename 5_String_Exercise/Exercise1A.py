'''
Exercise 1A: Create a string made of the first, middle and last character
Write a program to create a new string made of an input string’s first, middle, and last character.

Given:

str1 = "James"
Expected Output:

Jms

'''

str1 = "James"
print(str1[0], str1[2], str1[4])

# sample answer
str1 = "James"
print("Original String is", str1)

# Get first character
res = str1[0]

# Get string size
l = len(str1)
# Get middle index number
mi = int(l/2)
# Get middle character and add it to result
res = res + str1[mi]

# Get last character and add it to result
res = res + str1[l - 1]

print("New String", res)