'''
Exercise 2:
Remove and add item in a list
Write a program to remove the item present at index 4 
and add it to the 2nd position and at the end of the list.

Given:

list1 = [34, 54, 67, 89, 11, 43, 94]
Expected Output:

List After removing element at index 4  [34, 54, 67, 89, 43, 94]
List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
'''
list1 = [34, 54, 67, 89, 11, 43, 94]
tmp = list1.pop(4)
print(list1)
list1.insert(2, tmp)
print(list1)
list1.append(tmp)
print(list1)

# sample answer
'''
pop(index): Removes and returns the item at the given index from the list.
insert(index, item): Add the item at the specified position(index) in the list
append(item): Add item at the end of the list.
'''
sample_list = [34, 54, 67, 89, 11, 43, 94]

print("Original list:", sample_list)
element = sample_list.pop(4)
print("List After removing element at index 4", sample_list)

sample_list.insert(2, element)
print("List after Adding element at index 2", sample_list)

sample_list.append(element)
print("List after Adding element at last", sample_list)