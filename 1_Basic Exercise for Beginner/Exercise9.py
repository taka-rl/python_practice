'''
Exercise 9: Check Palindrome Number
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

Expected Output:

original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number
'''

#15分　解けず、解答確認した。
'''
def numcheck(num):
    
    num1 = num
    num2 = num.reverse()

    if num1 == num2:
        return "Yes. given number is palindrome number"
    else:
        return "No. given number is not palindrome number"


print("priginal number 121")
numcheck(str(121))
'''

#-------sample answer------
def palindrome(number):
    print("original number", number)
    original_num = number
    
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10
    
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")
        
palindrome(121)
palindrome(125)
        


