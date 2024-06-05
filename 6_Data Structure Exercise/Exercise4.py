'''
Exercise 4: Count the occurrence of each element from a list
Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.

Given:sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
Expected Output:Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
'''

# sample answer
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list", sample_list)

count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
        
print("Printing count of each item", count_dict)

'''
Python dictionary represents a mapping between a key and a value. 
In simple terms, a Python dictionary can store pairs of keys and values. 
Each key is linked to a specific value. Once stored in a dictionary, you can later obtain the value using just the key.
'''
print(count_dict.keys())
print(count_dict.values())
print(count_dict.items())
'''
keys():Returns the list of all keys present in the dictionary.
values():Returns the list of all values present in the dictionary
items():Returns all the items present in the dictionary. Each item will be inside a tuple as a key-value pair.
'''