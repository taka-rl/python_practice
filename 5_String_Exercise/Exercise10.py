'''
Exercise 10: 
Write a program to count occurrences of all characters within a string
Given:str1 = "Apple"
Expected Outcome:{'A': 1, 'p': 2, 'l': 1, 'e': 1}

'''
list = []
num = []
pre = ""
j = 0
str1 = "Apple"
for i in range(0, len(str1), 1):
    if str1[i] != pre:
        list.append(str1[i]) 
        pre = str1[i]
        num.append(int(1))
        j += 1
        
    elif str1[i] == pre:
        num[j-1] = num[j -1] + 1
        
    else:
        continue

for i in range(0, len(list), 1):
    print(list[i], num[i], end = " ")

print('\n')

# sample answer
str1 = "Apple"
# create a result dictionary
char_dict = dict()
for char in str1:
    count = str1.count(char)
    print(count)
    # add / update the count of a character
    char_dict[char] = count
    print(char_dict, count)
    
print('Result', char_dict)

'''
Creating a dictionary
There are following three ways to create a dictionary.

Using curly brackets: The dictionaries are created by enclosing the comma-separated Key: Value pairs inside the {} curly brackets. The colon ‘:‘ is used to separate the key and value in a pair.
Using dict() constructor:  Create a dictionary by passing the comma-separated key: value pairs inside the dict().
Using sequence having each item as a pair (key-value)

'''

        