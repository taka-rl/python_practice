'''
Exercise 7: Check if two sets have any elements in common. 
If yes, display the common elements
Given:

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
Expected output:

Two sets have items in common
{10}
'''
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

ans = set1 & set2
print("Two sets have items in common")
print(ans)

# sample answer
'''
The isdisjoint() method will find whether two sets are disjoint
i.e there are no common elements. This method will return true 
if they are disjoint otherwise it will return false.

'''
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

if set1.isdisjoint(set2):
    print("Two sets have no items in common")
else:
    print("Two sets have items in common")
    print(set1.intersection(set2))
    

## isdisjoint Example
color_set1 = {'violet', 'blue', 'yellow', 'red'}
color_set2 = {'orange', 'red'}
color_set3 = {'green', 'orange'}

# disjoint
print(color_set2.isdisjoint(color_set1))
# Output 'False' because contains 'red' as a common item

print(color_set3.isdisjoint(color_set1))
# Output 'True' because no common items