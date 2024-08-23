'''
Exercise 16: Calculate the cube of all numbers from 1 to a given number

Write a program to rint the cube of all numbers from 1 to a given number

Given:

input_number = 6

Expected output:

Current Number is : 1  and the cube is 1
Current Number is : 2  and the cube is 8
Current Number is : 3  and the cube is 27
Current Number is : 4  and the cube is 64
Current Number is : 5  and the cube is 125
Current Number is : 6  and the cube is 216
'''

input_number = 6
ans = 1

for i in range(1, input_number + 1, 1):
    for j in range(0, 3, 1):
        ans = ans * i
    print("Current Number is :", i, "and the cube is", ans)
    ans = 1

# sample answer

input_number = 6
for i in range(1, input_number + 1):
    print("Current Number is :", i, " and the cube is", (i * i * i))
    