'''
Exercise 2: Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers and in each iteration,
print the sum of the current and previous number.
'''
#11分 google先生有

print('Printing current and previous number sum in a range(10)')

preval = int(0)

s = 'Current Number '
s1 = ' Previous Number '
s2 = ' Sum: '

for i in range(10):
    sumval = i + preval
    print(s + str(i) + s1 + str(preval) + s2 + str(sumval))
    preval = i

#----------↓sample answer↓--------
print('Printing current and previous number and their sum in a range(10)')
previousNum = 0

for i in range(10):
    xSum = previousNum + i
    print("Current Number", i, "Previous Number ", previousNum, " Sum: ", previousNum + i)
    previousNum = i




