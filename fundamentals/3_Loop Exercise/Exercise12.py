'''
Exercise 12: Display Fibonacci series up to 10 terms
The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.

For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.

Expected output:

Fibonacci sequence:
0  1  1  2  3  5  8  13  21  34

'''

num1 = 0
num2 = 1
preval1, preval2 = 0, 0

print("Fibonacci swquence:")
print(num1, "\t", num2, end = "\t")
for i in range(1, 10, 1):
    if i == 1:
        ans = num1 + num2
        print(ans, end = '\t')
        preval1 = num2
        preval2 = ans
    else:
        ans = preval1 + preval2
        print(ans, end = '\t')
        preval1 = preval2
        preval2 = ans

# sample answer

# firsttwo numbers
num1, num2 = 0, 1
print("Fibonacci sequence:")

# run loop 10 times
for i in range(10):
    # print next number of a series
    print(num1, end = " ")
    # add last two numbers to get next number
    res = num1 + num2
    
    # update values
    num1 = num2
    num2 = res

        
    