'''
Exercise 3: Calculate the sum of all numbers from 1 to a given number
Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

Expected Output:

Enter number 10
Sum is:  55
'''

num = int(input("Enter number:"))
ans = 0
for i in range(1, num + 1):
    ans += i
print(ans)

### sample answer
s = 0
n = int(input("Enter number:"))

# run loop n times
# stop:n + 1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print("Sum is:", s)
