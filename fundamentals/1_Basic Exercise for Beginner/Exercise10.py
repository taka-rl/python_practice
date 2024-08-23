'''
Exercise 10: Create a new list from a two list using the following condition
Create a new list from a two list using the following condition

Given a two list of numbers, 
write a program to create a new list such that the new list should contain 
odd numbers from the first list and even numbers from the second list.

Given:

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
Expected Output:

result list: [25, 35, 40, 60, 90]

'''

#8分30秒 google検索有

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("list1 = ", list1)
print("list2 = ", list2)

resultList = []

for i in list1:
    if i % 2 != 0:
        resultList.append(i)

for j in list2:
    if j % 2 == 0:
        resultList.append(j)
        
print("result list:", resultList)

#---------sample answer--------

def merge_list(list1, list2):
    result_list = []
    
    for num in list1:
        if num % 2 != 0:
            result_list.append(num)
    
    for num in list2:
        if num % 2 == 0:
            result_list.append(num)
    
    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", merge_list(list1, list2))
