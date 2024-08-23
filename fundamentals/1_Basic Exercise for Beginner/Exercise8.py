'''
Exercise 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''
#4分 縦にはできたが、横に表示させれなかったため、解答見た。
for i in range(6):
    for j in range(i):
        print(i)
        
#---------sample answer-------

for num in range(10):
    for i in range(num):
        print(num, end = " ")
    print("\n")

        