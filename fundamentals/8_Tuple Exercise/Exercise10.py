'''
Exercise 10: Check if all items in the tuple are the same
tuple1 = (45, 45, 45, 45)
Expected output:True
'''

def chkAll(tuple1):
    tmp = tuple1[0]
    for i in tuple1:
        if i == tmp:
            continue
        else:
            return False
    return True

tuple1 = (45, 45, 45, 45)
print(all(tuple1))
print(chkAll(tuple1))

# sample answer
def check(t):
    return all(i == t[0] for i in t)
tuple1 = (45, 45, 45, 45)
print(check(tuple1))
