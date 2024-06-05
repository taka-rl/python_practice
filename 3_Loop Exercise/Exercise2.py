'''
Exercise 2: Print the following pattern
Write a program to print the following number pattern using a loop.

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

x, i = 1, 1
while x <= 5:
    if x / i == 0:
        print(x)
    else:
        print(x, end = ' ')
    x += 1
    i += 1

'''

for x in range(1, 6):
    for y in range(1, x + 1):
        print(y, end = ' ')
    print('')


### sample answer
print("Number Pattern ")
# Decide the row count. (above pattern contains 5 rows)
row = 5
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
for i in range(1, row + 1, 1):
    # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")