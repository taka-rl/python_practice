'''
Write a function to return True if the first and last number of a given list is same. 
If numbers are different then return False.

Given:
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

'''

#13分、google検索無し

def checkNum(arrayData):
    arrayBeg = arrayData[0]
    tmp = len(arrayData)
    arrayEnd = arrayData[tmp - 1]
    
    if arrayBeg == arrayEnd:
        return 'True'
    else:
        return 'False'

numbers_x = [10, 20, 30, 40, 10]
ans1 = checkNum(numbers_x)

numbers_y = [75, 65, 35, 75, 30]
ans2 = checkNum(numbers_y)

print("result is " + ans1)
print("result is " + ans2)


#---------sample answer---------

def first_last_same(numberList):
    print("Given list:", numberList)
    
    first_num = numberList[0]
    last_num = numberList[-1]
    
    if first_num == last_num:
        return True
    else:
        return False
    
numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))
