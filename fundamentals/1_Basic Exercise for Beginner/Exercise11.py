'''
Exercise 11: Write a Program to extract each digit
from an integer in the reverse order.
For example, If the given int is 7536, 
the output shall be “6 3 5 7“, with a space separating the digits.

'''

'''
def extractNum(num):
    
    chr = str(num)
    chrNum = []
    
    for i in chr:
        chrNum = chr[-i]
    
    return chrNum
   

print("Input value:", 7536)
print("Result:", extractNum(7536))
'''

#--------sample answer-------
number = 7536
print("Given number:", number)
while number > 0:
    digit = number % 10
    number = number // 10
    print(digit, end = ' ')
    
