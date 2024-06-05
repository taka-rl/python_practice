'''
Exercise 6: Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers
which are divisible by 5

Expected Output:

Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55

'''
#9分

list = [10, 20, 33, 46, 55]
print("Given list is ", list)

for i in list:
    if i%5 == 0:
        print(i)

#---------sample answer--------

num_list = [10, 20, 33, 46, 55]
print("Given list:", num_list)
print("Divisible by 5:")
for num in num_list:
    if num % 5 == 0:
        print(num)
        

