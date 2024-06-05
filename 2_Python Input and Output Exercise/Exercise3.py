'''
Exercise 3: Convert Decimal number to octal 
using print() output formatting
Given:

num = 8
Expected Output:

The octal number of decimal number 8 is 10
'''

def dec2oct(number):
    tmp = number
    tmp1 = ""
    while int(tmp) != int(0):
        tmp1 = str(tmp % 8) + tmp1
        tmp = round(tmp / 8)

    answer = tmp1
    return answer
            
num = 10

print("The octal number of decimal number", num, "is", dec2oct(num))

#-------sample answer------
num = 10
print('%o' % num)
print(oct(num))


