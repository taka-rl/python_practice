'''
Exercise 8: Update set1 by adding items from set2, except common items
Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:

{70, 10, 20, 60}

'''

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.difference(set2))
print(set2.difference(set1))
ans1 = set1.difference(set2)
ans2 = set2.difference(set1)
ans1.update(ans2)
print(ans1)


# sample answer
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.symmetric_difference_update(set2)
print(set1)

'''
symmetric_difference_upda

In addition to the symmetric_difference(), there is one more method called symmetric_difference_update(). 
There are two main differences between these two methods.

The symmetric_difference() method will not update the original set 
while symmetric_difference_update() will update the original set with the unique elements from both sets.

'''
#Example

color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}

# symmetric difference
unique_items = color_set.symmetric_difference(remaining_colors)
print(unique_items)
# output {'yellow', 'green', 'violet', 'red', 'blue', 'orange'}
# original set after symmetric difference
print(color_set)
# {'yellow', 'green', 'indigo', 'blue', 'violet'}

# using symmetric_difference_update()
color_set.symmetric_difference_update(remaining_colors)
# original set after symmetric_difference_update()
print(color_set)
# {'yellow', 'green', 'red', 'blue', 'orange', 'violet'}