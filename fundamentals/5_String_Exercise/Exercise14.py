'''
Exercise 14: Remove empty strings from a list of strings
Given:

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
Expected Output:

Original list of sting
['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

After removing empty strings
['Emma', 'Jon', 'Kelly', 'Eric']

'''

'''
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
str_list = filter(str_list, "")
print(str_list)

for char in str_list:
    if filter(char, ""):
        print(char)
'''

# sample answer 
# solution1:Using the loop and if condition
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res_list = []
for s in str_list:
    # check for non empty string
    # if it is not an empty, it's appended to res_list.
    if s:
        res_list.append(s)
print(res_list)

# solution2:Using the built-in function filter()
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
#use built-in function filter to filter empty value
new_str_list = list(filter(None, str_list))
print("After removing empty strings")
print(new_str_list)
