# 多行匹配模式
import re

print('=========1=========')
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
... multiline comment */
... ''' ## C语言分割注释
print(comment.findall(text1))
print(comment.findall(text2))

## 修改模式字符串，增加对换行的支持
print('=========2=========')
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))
## (?:.|\n) 指定了一个非捕获组（定义了一个仅仅用来作匹配，而不能通过单独捕获或者编号的组。）

## re.DOTALL 可以让(.)匹配包括换行符在内的任意字符。
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))








