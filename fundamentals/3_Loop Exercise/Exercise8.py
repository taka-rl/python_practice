'''
Exercise 8: Print list in reverse order using a loop
Given:
list1 = [10, 20, 30, 40, 50]
Expected output:
50
40
30
20
10
'''

# sample answer1
list1 = [10, 20, 30, 40, 50]
# reverse list
new_list = reversed(list1)
# iterate reversed list
for item in new_list:
    print(item)

# sample answer2
list1 = [10, 20, 30, 40, 50]
# get list size
# len(list1) -1 :because index start with 0
# iterate list in reverse order
# start from last item to first
size = len(list1) - 1
for i in range(size, -1, -1):
    print(list1[i])

    
