'''
Exercise 9: Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2]
Expected Output:24
'''

x = [4, 6, 8, 24, 12, 2]
iMax = 0
for i in x:
    if i >= iMax:
        iMax = i
    else:
        continue
print(iMax)

# sample answer
x = [4, 6, 8, 24, 12, 2]
print(max(x))






