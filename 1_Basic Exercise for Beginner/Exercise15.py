'''
Exercise 15: Write a function called exponent(base, exp) that returns 
an int value of base raises to the power of exp.
Note here exp is a non-negative integer, and the base is an integer.

Expected output
Case 1:

base = 2
exponent = 5

2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

Case 2:

base = 5
exponent = 4

5 raises to the power of 4 is: 625 
i.e. (5 *5 * 5 *5 = 625)
'''

#12分 google検索なし

def exponent(base, exp):
    result = 1
    
    if base == 0:
        return 0
    elif exp == 0:
        return 1
    else:
        for i in range(1, exp + 1):
            result *= base
        
    return result

print( "the answer :", exponent(5, 4))


#-----sample answer-----
def exponent1(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raise to the power of", exp, "is", result)
    
exponent1(5, 4)