'''
Exercise 1:
Create a list by picking an odd-index items from the first list and even index items from the second
Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element
from the list l1 and even index elements from the list l2.

Given:

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
Expected Output:

Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]

Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
'''

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = []

len1 = len(l1)
len2 = len(l2)

for i in range(1, len1, 2):
    l3.append(l1[i])

for j in range(0, len2 + 1, 2):
    l3.append(l2[j])

print(l3)

# sample answer
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list() # making an empty list [].

odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements = list2[0::2]
print("Element at even-index positions from list two")
print(even_elements)

print("Printing Final third list")
print(res)
res.extend(odd_elements)
print(res)
res.extend(even_elements)
'''
The extend method will accept the list of elements and add them at the end of the list.
We can even add another list by using this method.
'''
print(res)



    
