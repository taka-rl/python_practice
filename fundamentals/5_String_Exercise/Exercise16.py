'''
Exercise 16: Removal all characters from a string except integers
Given:str1 = 'I am 25 years and 10 months old'
Expected Output:2510
'''

import re
str1 = 'I am 25 years and 10 months old'
# 0-9以外を""に置換"
ans = re.sub(r'[^0-9]', "", str1)
print(ans)

ans = ""
for char in str1:
    if not char.isalpha() and not char == " ":
        ans = ans + char
print(ans)

# sample answer
str1 = 'I am 25 years and 10 months old'
print("Original string is", str1)
# Retain Numbers in String
# Using list comprehension + join() + isdigit()
res = "".join([item for item in str1 if item.isdigit()])
print(res)