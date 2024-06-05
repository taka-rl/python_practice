'''
Exercise 9: Calculate the sum and average of the digits present in a string

Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

Given:str1 = "PYnative29@#8496"
Expected Outcome:Sum is: 38 Average is  6.333333333333333

'''
def chkString(str1):
    sum = 0
    ave = 0
    cnt = 0
    
    for i in str1:
        if i.isdigit():
            sum += int(i)
            cnt += 1
        
    ave = sum / cnt
    print("Sum is:", sum, "Average is", ave)

str1 = "PYnative29@#8496"
chkString(str1)

# sample answer
# solution1
# solution1 is the same as mine.

# solution2
# use regular expression
import re

input_str = "PYnative29@#8496"
digit_list = [int(num) for num in re.findall(r'\d', input_str)]
print('Digits:', digit_list)

# use the built-in function sum
total = sum(digit_list)

# average = sum / count of digits
avg = total / len(digit_list)
print("sum is:", total, "Average is:", avg)

'''
https://pynative.com/python/regex/

・What are regular expressions?
The Regex or Regular Expression is a way to define a pattern for searching or manipulating strings.
We can use a regular expression to match, search, replace, and manipulate inside textual data.

The re module
We will start this tutorial by using the RE module, a built-in Python module 
that provides all the required functionality needed for handling patterns and regular expressions.
Type import re at the start of your Python file, and you are ready to use the re module's methods 
and special characters. To get to know the RE module's functionality, methods, and attributes, use the help function.

'''


