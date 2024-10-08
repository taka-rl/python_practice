'''
Exercise 5: Display numbers from a list using loop

Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
Given:

numbers = [12, 75, 150, 180, 145, 525, 50]
Expected output:

75
150
145

'''

numbers = [12, 75, 150, 180, 145, 525, 50]
print("the given numbers are", numbers)

for i in numbers:
    if i % 5 == 0 and i <= 150:
        print(i)
        
    if i >= 500:
        break

# sample answer
numbers = [12, 75, 150, 180, 145, 525, 50]
# iterate each item of a list
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    # check if number is divisible by 5
    elif item % 5 == 0:
        print(item)

# check

ans1 = 15>15
ans2 = 15 >= 15
print(ans1, ans2)