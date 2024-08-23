'''
Exercise 17: Find the sum of the series upto n terms
Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

Given:

# number of terms
n = 5
Expected output:
24690
'''

# number of terms
n = 5
ans, tmp = 0, 0

for i in range(1, n + 1, 1):
    tmp = (tmp * 10) + 2
    ans += tmp
print(ans)

# sample answer
n = 5
# first number of sequence
start = 2
sum_seq = 0

# run loop n times
for i in range(0, n):
    print(start, end = "+")
    sum_seq += start
    # calculate the next term
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)
