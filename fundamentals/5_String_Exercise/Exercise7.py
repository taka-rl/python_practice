'''
Exercise 7: String characters balance Test
Write a program to check if two strings are balanced. 
For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. 
The character’s position doesn’t matter.

Given:
Case 1:
s1 = "Yn"
s2 = "PYnative"
Expected Output:True

Case 2:
s1 = "Ynf"
s2 = "PYnative"
Expected Output:False
'''

def chkstring(char1, char2):
    jud = False
    l1 = len(char1)
    l2 = len(char2)
    for i in range(0, l1, 1):
        for j in range(0, l2, 1):
            if ~jud:
                if char1[i] == char2[j]:
                    jud = True
                    break
                else:
                    jud = False
            elif jud:
                if char1[i] == char2[j]:
                    continue
    print(jud)

s1 = "Yn"
s2 = "PYnative"
chkstring(s1, s2)

s1 = "Ynf"
s2 = "PYnative"
chkstring(s1, s2)

# sample answer
def string_balance_test(s1, s2):
    flag = True
    for char in s1:
        print(char)
        if char in s2:
            print(char)
            continue
        else:
            print(char)
            flag = False
        
    return flag

s1 = "Yn"
s2 = "PYnative"
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)

s1 = "Ynf"
s2 = "PYnative"
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)