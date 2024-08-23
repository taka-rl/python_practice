'''
Exercise 5: Count all letters, digits, 
and special symbols from a given string
Given:
str1 = "P@#yn26at^&i5ve"
Expected Outcome:

Total counts of chars, digits, and symbols 
Chars = 8 
Digits = 3 
Symbol = 4

'''

str1 = "P@#yn26at^&i5ve"
chars = 0
digits = 0
symbol = 0

for i in str1:
    if i.isalpha():
        chars += 1
    elif i.isdigit():
        digits += 1
    else:
        symbol += 1

print("Chars:", chars, "Digits:", digits, "Symbol:", symbol)


# sample answer
def find_digits_chars_symbols(sample_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    for char in sample_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        # if it is not letter or digit then it is special symbol
        else:
            symbol_count += 1
    print("Chars =", char_count, "Digits =", digit_count, "Symbol = ", symbol_count)

sample_str = "P@yn2at&#i5ve"
print("total counts of chars, Digits, and symbols")
find_digits_chars_symbols(sample_str)
            