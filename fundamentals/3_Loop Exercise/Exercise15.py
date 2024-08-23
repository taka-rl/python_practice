'''
Exercise 15: Use a loop to display elements 
from a given list present at odd index positions

Given:

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Note: list index always starts at 0

Expected output:

20 40 60 80 100

'''

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in my_list:
    j = i // 10
    if j % 2 == 0:
        print(i, end =" ")
        

# sample answer
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# start from index 1 with step 2( means 1, 3, 5, and so on)
for i in my_list[1::2]:
    print(i, end = " ")

    
    