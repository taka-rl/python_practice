'''
Exercise 4: Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new string.

For example:

remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.
Note: n must be less than the length of the string.
'''
#18分 google先生有

word = input("input string: ")

num = int(input("input number: "))

newWord = word[num:]
#
#for i in range(num):
#    newWord = word[i].replace
#    print(newWord)

print(newWord)

#------sample answer------

def remove_chars(word,n):
    print("Original string:", word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))
