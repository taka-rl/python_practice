'''
Exercise 6: Create a recursive function
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

A recursive function is a function that calls itself again and again.

Expected Output:

55

'''

'''
def cal(num1, num2):
    ans = 0
    for i in range(num1, num2 + 1, 1):
        
        def recursivefun(num1, num2):
    
    ans = 
    
print(cal(num1, num2))

ans = 0
for i in range(1, 11, 1):
    ans += i
print(ans)
'''

def addition(num):
    if num:
        #call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0
    
res = addition(10)
print(res)