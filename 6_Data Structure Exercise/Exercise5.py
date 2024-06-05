'''
Exercise 5: Create a Python set such that it shows the element from both lists in a pair
Given:
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
Expected Output:
Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}
'''

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
print("First list:", first_list)
print("Second list:", second_list)
ans = dict()
length = len(second_list)
ans = first_list
for i in range(0, length, 1):
    ans[i] = second_list[i]
print(ans)

# sample answer
'''
https://pynative.com/python-dictionaries/#h-creating-a-dictionary
https://www.sejuku.net/blog/24122

'''
'''
Use the zip() function. This function takes two or more iterables (like list, dict, string),
aggregates them in a tuple, and returns it.
Tuples are ordered collections of heterogeneous data that are unchangeable. 
Heterogeneous means tuple can store variables of all types.
'''
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
print("First list:", first_list)
print("Second list:", second_list)

result = zip(first_list, second_list)
result_set = set(result)
print(result_set)





