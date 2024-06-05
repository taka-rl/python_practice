'''
Exercise 2: Return a new set of identical items from two sets
Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:

{40, 50, 30}
'''

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
comset = set1 & set2
print(comset)
comset = set1 | set2
print(comset)

'''
・Union
All the items of both Sets will be returned. Only the duplicate items will be dropped.
|
union()
・Intersection
Only the items common in both sets will be returned.
&
intersection()

'''


# sample answer
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))
