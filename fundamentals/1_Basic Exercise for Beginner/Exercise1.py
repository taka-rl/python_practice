'''
Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers return their product 
only if the product is equal to or lower than 1000, else return their sum.
'''

def calc(num1, num2):
    
    ans = num1 * num2
    if ans >= 1000:
        return num1 + num2
    else:
        return ans

print(calc(20, 30))

print(calc(40, 30))

#-----------↓sample answer------------

def calc(num1, num2):
    
    ans = num1 * num2
    if ans <= 1000:
        return ans
    else:
        return num1 + num2

print(calc(20, 30))

print(calc(40, 30))