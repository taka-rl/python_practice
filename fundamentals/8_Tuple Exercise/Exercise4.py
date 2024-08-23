'''
Exercise 4: Unpack the tuple into 4 variables
Write a program to unpack the following tuple into four variables and display each variable.

Given:

tuple1 = (10, 20, 30, 40)
Expected output:

tuple1 = (10, 20, 30, 40)
# Your code
print(a) # should print 10
print(b) # should print 20
print(c) # should print 30
print(d) # should print 40
'''

a, b, c, d = 0, 0, 0, 0
tuple1 = (10, 20, 30, 40)

a = tuple1[0]
b = tuple1[1]
c = tuple1[2]
d = tuple1[3]

print(a, b, c, d)

# sample answer
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)
