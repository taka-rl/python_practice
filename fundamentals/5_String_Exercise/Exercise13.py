'''
Exercise 13: Split a string on hyphens
Write a program to split a given string on hyphens and display each substring.

Given:
str1 = Emma-is-a-data-scientist
Expected Output:

Displaying each substring

Emma
is
a
data
scientist

'''

str1 = "Emma-is-a-data-scientist"
print("Given String is:", str1)

ans = ""
print("Displaying each substring:")
for char in str1:
    if char != "-":
        ans = ans + char
    elif char == "-":
        print(ans)
        ans = ""
        
'''
↑自分のプログラムだと
Emma
is
a
data
scientist:←これが表示されない。

'''

# sample answer
str1 = "Emma-is-a-data-scientist"
print("Original String is:", str1)

# split string
sub_strings = str1.split("-")
print(sub_strings) # → ['Emma', 'is', 'a', 'data', 'scientist']

print("Displaying each substring")
for sub in sub_strings:
    print(sub)
    