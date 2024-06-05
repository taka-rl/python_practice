'''
I need to review from 4 to 6.

Exercise 6: 
Find the intersection (common) of two sets and remove those elements from the first set

See: Python Set

Given:

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
Expected Output:

Intersection is  {57, 83, 29}
First Set after removing common element  {65, 42, 78, 23}
'''

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
print("First list:", first_set)
print("Second list:", second_set)

print(type(first_set))

# sample answer
# Use the intersection() and remove() method of a set
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
print("First list:", first_set)
print("Second list:", second_set)

intersection = first_set.intersection(second_set)
print("Intersection is", intersection)
for item in intersection:
    first_set.remove(item)

print("First Set after removing common element", first_set)
