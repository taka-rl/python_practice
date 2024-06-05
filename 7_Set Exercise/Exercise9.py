'''
Exercise 9: Remove items from set1 that are not common to both set1 and set2
Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:

{40, 50, 30}

'''

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection(set2)
print(set1)

print(set1.intersection(set2))

set1.intersection_update(set2)
print(set1)

'''
Intersection update
In addition to the above intersection() method, we have one more method called intersection_update().

There are two key differences between intersection() and intersection_update()

intersection() will not update the original set but intersection_update() will update the original set with only the common elements.
intersection() will have a return value which is the new set with common elements between two or more sets whereas intersection_update() will not have any return value.
'''