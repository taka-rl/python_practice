'''
Exercise 8: Sort a tuple of tuples by 2nd item
Given:

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
Expected output:

(('c', 11), ('a', 23), ('d', 29), ('b', 37))

'''

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

'''
tmp = ()
length = len(tuple1)
iniVal = tuple1[0][1]
for i in range(0, length, 1):
    if tuple1[i][1] >= iniVal:
        continue
    
    else:
        iniVal = tuple1[i][1]
        tmp.append(tuple1[i])
        
tmp.append(tuple1[i])
'''

# sample answer
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
tuple1 = tuple(sorted(tuple1, key = lambda x:x[1]))
print(tuple1)

list_of_tuples = ((1, 50), (1, 20),  (1, 30))

# another example related to this exercise
# https://bobbyhadz.com/blog/python-sort-list-of-tuples-by-second-element
# ✅ sort list of tuples by second element (ascending order)
sorted_list = sorted(
    list_of_tuples,
    key=lambda t: t[1]
)

print(sorted_list)  # 👉️ [(1, 20), (1, 30), (1, 50)]



