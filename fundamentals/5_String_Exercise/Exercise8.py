'''
Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
Write a program to find all occurrences of “USA” in a given string ignoring the case.

Given:str1 = "Welcome to USA. usa awesome, isn't it?"
Expected Outcome:The USA count is: 2
'''

def strCheck(char, str1):
    cnt = 0
    for i in char:
        if i in str1:
            cnt += 1
        else:
            continue
    print(cnt)

char = "USA"
str1 = "Welcome to USA. usa awesome, isn't it?"
strCheck(char, str1)


# sample answer
# lower → upper でも実行可能。
str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"

# convert string to lowercase
temp_str = str1.lower()
print(temp_str)
# use count function
count = temp_str.count(sub_string.lower())
print("The USA count is:", count)
            