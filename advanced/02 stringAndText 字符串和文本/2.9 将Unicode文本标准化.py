# 处理 Unicode 字符串，需要确保所有字符串在底层有相同的表示。

## Unicode 中，某些字符能够用多个合法的编码表示。
print('=========1=========')
s1 = 'Spicy Jalape\u00f1o' # 使用整体字符”ñ” (U+00F1)
s2 = 'Spicy Jalapen\u0303o' # 使用拉丁字母”n”后面跟一个”~”的组合字符 (U+0303)
print(s1)
print(s2)
print(len(s1))
print(len(s2))

## 在需要比较字符串的程序中使用字符的多种表示会产生问题。
## 修正这个问题，可以使用unicodedata 模块先将文本标准化。
import unicodedata
print('=========2=========')
t1 = unicodedata.normalize('NFC', s1) # NFC表示字符应该是整体组成(可能的化使用单一编码)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(ascii(t1))
print(ascii(t2))
t3 = unicodedata.normalize('NFD', s1) # NFD表示应该分解为多个组合字符表示
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)
print(ascii(t3))
print(ascii(t4))

## Python 同样支持扩展的标准化形式 NFKC、NFKD 处理某些字符时候增加了额外兼容特性
print('=========3=========')
s = '\ufb01'
print(s)
print(unicodedata.normalize('NFD', s))
print(unicodedata.normalize('NFKD', s))
print(unicodedata.normalize('NFKC', s))

## 标准化对于要以一致方式处理Unicode文本的程序非常重要，当处理来自用户输入的字符串而我们很难控制编码时候更甚
t1 = unicodedata.normalize('NFD', s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))
## unicodedata也是测试字符类的工具函数，combining()可以测试一个字符是否为和音字符

# http://www.unicode.org/faq/normalization.html
# https://nedbatchelder.com/text/unipain.html



















