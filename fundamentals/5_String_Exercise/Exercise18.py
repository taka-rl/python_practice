'''
Exercise 18: Replace each special symbol with # in the following string
Given:
str1 = '/*Jon is @developer & musician!!'
Expected Output:
##Jon is #developer # musician##

'''
import re
str1 = '/*Jon is @developer & musician!!'
res = ""

res = re.sub(r'[^0-9\w\s]', "#", str1)
print(res)

# sample answer
'''
https://docs.python.org/ja/3.9/library/string.html#string.punctuation
特殊文字:!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.→string.punctuation
*使用するためには、import string が必要。
他の例:アルファベット
小文字:string.ascii_lowercase
大文字:string.ascii_uppercase

空白:string.whitespace
'''
import string
str1 = '/*Jon is @developer & musician!!'
print("The original string is:", str1)

# Replace punctuations with #
replace_char = "#"

# string.punctuation to get the list of all special symbols
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)
    
print("The strings after replacement:", str1)

        

