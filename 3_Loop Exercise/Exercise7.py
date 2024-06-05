'''
Exercise 7: Print the following pattern
Write a program to use for loop to print the following reverse number pattern

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1

'''

'''
参考ページ
https://www.python.ambitious-engineer.com/archives/1757#reversed
'''

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end = ' ')
    print("\t")

#sample answer
n = 5
k = 5
for i in range(0, n + 1):
    for j in range(k-1, 0, -1):
        print(j, end = " ")
    print()