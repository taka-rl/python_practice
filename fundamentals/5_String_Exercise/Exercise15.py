'''
Exercise 15: Remove special symbols / punctuation from a string
Given:str1 = "/*Jon is @developer & musician"
Expected Output:"Jon is developer musician"

'''

str1 = "/*Jon is @developer & musician"
ans = ""
for char in str1:
    if char.isalpha() or char == " ":
        ans = ans + char
ans = ans.replace("  ", " ")
print(ans)

# sample answer
# solution1:Use string functions translate() and maketrans().
'''
Use the translate() function to get a new string where specified characters are replaced with the character described in a dictionary or a mapping table.
Use the maketrans() function to create a mapping table.
'''
import string
str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)
new_str = str1.translate(str.maketrans('', '', string.punctuation))
print("New string is ", new_str)

# solution2:Using regex replace pattern in a string
'''
https://pynative.com/python-regex-replace-re-sub/
https://docs.python.org/ja/3.9/library/re.html

[]:文字の集合を指定するのに使います。
補集合 をとって範囲内にない文字にマッチできます。集合の最初の文字が '^' なら、集合に 含まれない 全ての文字にマッチします。
例えば、 [^5] は '5' を除くあらゆる文字にマッチし、 [^^] は '^' を除くあらゆる文字にマッチします。 ^ は集合の最初の文字でなければ特別の意味を持ちません。

^:(キャレット) 文字列の先頭にマッチし、 MULTILINE モードでは各改行の直後にもマッチします。

\w
Unicode (str) パターンでは:
Unicode 単語文字にマッチします。これはあらゆる言語で単語の一部になりうるほとんどの文字、数字、およびアンダースコアを含みます。
ASCII フラグが使われているなら、 [a-zA-Z0-9_] のみにマッチします。

8 ビット (bytes) パターンでは:
ASCII 文字セットで英数字と見なされる文字にマッチします。これは [a-zA-Z0-9_] と等価です。
LOCALE フラグが使われているなら、現在のロケールで英数字と見なされる文字およびアンダースコアにマッチします。

\s
Unicode (str) パターンでは:
Unicode 空白文字 (これは [ \t\n\r\f\v] その他多くの文字、例えば多くの言語におけるタイポグラフィ規則で定義されたノーブレークスペースなどを含みます) にマッチします。
ASCII フラグが使われているなら、[ \t\n\r\f\v] のみにマッチします。

8 ビット (bytes) パターンでは:
ASCII 文字セットで空白文字と見なされる文字にマッチします。これは [ \t\n\r\f\v] と等価です。

re_sub(r,)
r:エスケープシーケンス
エスケープシーケンスとは、例えば複数行にわたる文字列を定義したい場合、
文字列の中に改行を表す文字を入力する必要があります。
このような特殊な文字を表すのに使用するもの
→https://www.javadrive.jp/python/string/index2.html#section1

'''
import re

str1 = "/*Jon is @developer & musician"
print("Original string is:", str1)

# replace special symbols with ''
res = re.sub(r'[^\w\s]', '', str1)
print("New string is:", res)


# res = re.sub(r'[^\w\s]', '', str1) → アルファベットと空白の組み合わせ以外が""に置換される。
# w:[a-zA-Z0-9_]
# s:whitespace
# → replace the one without only character with space ""
