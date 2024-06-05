'''
Exercise 4: Display float number with 2 decimal places using print()
Given:

num = 458.541315
Expected Output:

458.54
'''
#解答見た。%.2fは浮かんだが、文法が分からず・・・

num = 458.541315
print('%.2f' % num)

#変換指定子は整数が%d、浮動小数点が%f、文字列が%s
#using '%.x' you can decide to show the number of digits
# (x:depends on how many digits you want to show)
#sample
s = 'Alice'
i = 25
ff = 234.3123
print('Alice is %d years old' % i)
# Alice is 25 years old
print('%s is %d years old %.3f' % (s, i, ff))
# Alice is 25 years old