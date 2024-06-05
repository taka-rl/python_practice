'''
Exercise 12: Find the last position of a given substring
Write a program to find the last position of a substring “Emma” in a given string.

Given:str1 = "Emma is a data scientist who knows Python. Emma works at google."
Expected Output:Last occurrence of Emma starts at index 43

'''
str1 = "Emma is a data scientist who knows Python. Emma works at google."
str2 = "Emma"
print("Given String:", str1, "Searched word", str2)

pos =str1.rfind(str2)
print("Last occurrence of Emma starts at index", pos)

'''
find():search a word from the left side of it and return the position.
rfind():search a word from the right side of it and return the position.

'''
 