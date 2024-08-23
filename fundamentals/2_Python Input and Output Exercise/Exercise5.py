'''
Exercise 5: Accept a list of 5 float numbers as an input from the user
Refer:
Expected Output:
[78.6, 78.6, 85.3, 1.2, 3.5]
'''
#解答見た。

#numbers = print(float(input("input 5 float numbers:").split()))
#print("Expected Output:", numbers)

'''
numbers = []
print("input 5 float numbers")
for i in range(5):
    numbers[i] = print(input("input float numbers:"))

numbers = float(numbers)

print("Expected Output:", numbers)
'''

#-----sample answer-------
numbers = []
#5 is the list size
#run loop 5 times
for i in range(0, 5):
    print("Enter number at location", i, ":")
    #accept float number from user
    item = float(input())
    #add it to the list
    numbers.append(item)

print("User list:", numbers)