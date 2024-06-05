'''
Exercise 3: Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an even index number.

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
'''

#23分 google検索有

word = input("input string : ")
#strword = "pynative"
strNum = len(word)
for i in range(strNum):
    if i%2 == 0:
        #print(word(i))
        print(i, word[i])


#--------↓sample answer1--------
#accept input string from a user
word = input("Enter word:")
print("Original String:", word)

#get the length of a string
size = len(word)

print("Printing only even index chars")

#iterate a each character of a string
#start: 0 to start with first character
#stop: size-1 because index starts with 0
#step: 2 to get the characters present at even index like 0, 2, 4
for i in range(0, size -1, 2):
    print("index[", i, "]", word[i])

#--------↓sample answer2--------
word = input('ENter word:')
print("Original String:", word)

x = list(word)
for i in x[0::2]:
    print(i)
