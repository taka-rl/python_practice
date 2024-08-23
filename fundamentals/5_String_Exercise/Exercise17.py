'''
Exercise 17: Find words with both alphabets and numbers
Write a program to find words with both alphabets and numbers from an input string.

Given:
str1 = "Emma25 is Data scientist50 and AI Expert"
Expected Output:
Emma25
scientist50
'''

str1 = "Emma25 is Data scientist50 and AI Expert"
tmp = str1.split(" ")
length = len(tmp)

for i in range(0, length, 1):
    alpa = False
    num = False
    for char in tmp[i]:
        if char.isalpha():
            alpa = True
        if char.isdigit():
            num = True
            
    if alpa == True and num == True:
        print(tmp[i])

# sample answer
str1 = "Emma25 is Data scientist50 and AI Expert"
print("The original string is:", str1)

res = []
temp = str1.split()

# Words with both alphabets and numbers
# isdigit() for numbers + isalpha() for alphabets
# use any() to check each character

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

print("Displaying words with alphatets and numbers")
for i in res:
    print(i)
    
'''
any():引数に指定したイテラブルオブジェクトの要素のいずれかがTrueと判定されるとTrueを返す。すべてFalseであればFalse。

print(any([True, False, False]))
# True

print(any([False, False, False]))
# False

any()は以下のコードと等価。
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
    


'''
            

