'''
Exercise 6: Create a mixed String using the following rules
Given two strings, s1 and s2. Write a program to 
create a new string s3 made of the first char of s1, 
then the last char of s2, Next, the second char of s1 and second last char of s2, 
and so on. Any leftover chars go at the end of the result.

Given:
s1 = "Abc"
s2 = "Xyz"
Expected Output:AzbycX

'''

def madestring(char1, char2):
    #ans = []
    ans = ""
    for i in range(0, len(char1), 1):
        #ans.append(s1[i])
        #ans.append(s2[-i-1])
        ans += s1[i] + s2[-i-1]
    print(ans)

s1 = "Abc"
s2 = "Xyz"
madestring(s1, s2)

# sample answer
s1 = "Abc"
s2 = "Xyz"

# get string length
s1_length = len(s1)
s2_length = len(s2)

# get length of a bigger string
length = s1_length if s1_length > s2_length else s2_length
result = ""

# reverse s2
s2 = s2[:: -1]

# iterate string
# s1 ascending and s2 descending
for i in range(length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)