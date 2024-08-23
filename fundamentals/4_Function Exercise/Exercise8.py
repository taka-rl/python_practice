'''
Exercise 8: Generate a Python list of all the even numbers between 4 to 30
Expected Output:

[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

'''
def genList(min, max, index):
    for i in range(min, max, index):
        print(i, end = " ")
    
    print("\n")
    print(list(range(min, max, index)))
genList(4, 30, 2)



#sample answer
print(list(range(4, 30, 2)))






