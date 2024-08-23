'''
Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
* * * * *  
* * * *  
* * *
* *
*
'''
#5分10秒 google検索有

#for i in range(5):
#    for j in range(5 - i):
#        print('*', end = ' ')
#    print("\t\t")
    
for i in range(6, 0, -1):
    for j in range(i, 0, -1):
        print('*', end = ' ')
    print("")

