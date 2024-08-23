'''
Exercise 6: Count the total number of digits in a number
Write a program to count the total number of digits in a number using a while loop.

For example, the number is 75869, so the output should be 5.

'''
number = int(75869)
cnt = 0
while number > 0:
    number = number // 10
    cnt += 1
print("桁数:", cnt)

'''
//: 切り捨て除算

https://www.tohoho-web.com/python/operators.html#arithmetic

'''

# sample answer
num = 75869
count = 0
while num != 0:
    # floor division
    # to reduce the last digit from number
    num = num // 10
    
    # increment counter by 1
    count = count + 1
print("Total digits are:", count)




