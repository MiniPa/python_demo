# 最短匹配模式
## 在用regex匹配某个文本模式，但找到的是模式的最长可能匹配，而你想修改它成查找最短可能匹配
import re

## 如下案例
print('=========1=========')
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1)) # ['no.']

text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2)) # ['no." Phone says "yes.']
## r'\"(.*)\"' 是匹配被双引号包含的文本，*是贪婪的，会查找最长的可能匹配

## 修正
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2)) # ['no.', 'yes.']

## 点（.）匹配除换行外任何字符，在* +等后添加?，可强制匹配算法改成寻找最短的可能匹配








