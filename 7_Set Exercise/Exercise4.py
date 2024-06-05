'''
Exercise 4: Update the first set with items that don’t exist in the second set
Given two Python sets, write a Python program to update the first set with items 
that exist only in the first set and not in the second set.

Given:
set1 = {10, 20, 30}
set2 = {20, 40, 50}
Expected output:
set1 {10, 30}
'''

set1 = {10, 20, 30}
set2 = {20, 40, 50}
print(set1.difference(set2))

# sample answer

'''
Difference update
In addition to the difference(), there is one more method called difference_update(). 
There are two main differences between these two methods.

The difference() method will not update the original set while difference_update() will update the original set.
The difference() method will return a new set with only the unique elements from the set on which this method was called.
difference_update() will not return anything.

'''
set1 = {10, 20, 30}
set2 = {20, 40, 50}

# print(set1.difference_update(set2))
# → return "None"
set1.difference_update(set2)
print(set1)


