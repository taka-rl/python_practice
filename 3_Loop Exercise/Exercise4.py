'''
Exercise 4: Write a program to print multiplication table of a given number
For example, num = 2 so the output should be

2
4
6
8
10
12
14
16
18
20

'''

num = int(input("Enter number:"))
for i in range(1, 11, 1):
    print(i * num)

# sample question
n = 2
# stop: 11(because range never include stop number in result)
# run loop 10 times
for i in range(1, 11, 1):
    # 2 * i (current number)
    product = n * i
    print(product)


