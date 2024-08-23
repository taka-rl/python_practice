'''
Exercise 1B: Create a string made of the middle three characters
Write a program to create a new string 
made of the middle three characters of an input string.

Given:

Case 1
str1 = "JhonDipPeta"
Output:Dip

Case 2
str2 = "JaSonAy"
Output:Son

'''

str1 = "JhonDipPeta"
str2 = "JaSonAy"

len1, len2 = len(str1), len(str2)
mi1, mi2 = int(len1 / 2), int(len2 / 2)
ans1, ans2 = str1[mi1 - 1: mi1 + 2], str2[mi2 - 1: mi2 + 2]

print(ans1, ans2 , len1, mi1)

# sample answer

def getMidStr(string):
    l = len(string)
    m = int(l / 2)
    ans = string[m - 1: m + 2]
    print("Middle three chars are:", ans)

getMidStr("JhonDipPeta")
getMidStr("JaSonAy")