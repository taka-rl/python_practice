'''
Exercise 18: Print the following pattern
Write a program to print the following start pattern using the for loop

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''

num = 5
for i in range(1, num, 1):
    for j in range(0, i, 1):
        print('*', end = " ")
    print("\t")

for k in range(num, 0, -1):
    for m in range(k, 0, -1):
        print('*', end = " ")
    print("\t")    


# sample answer
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

