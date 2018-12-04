# 字符串开头或结尾匹配
filename = '__init__.txt'

print('=========1===========')
print(filename.endswith('.txt'))
print(filename.startswith('spam'))

## 检查多种匹配可能
import os
print('=========2===========')
filenames = os.listdir('.')
print(filenames)

filenames2 = [name for name in filenames if name.endswith(('.c', '.py')) ]
print(filenames2)
filenames3 = any(name.endswith('.c') for name in filenames)
print(filenames3)

## 下面方法需要一个元组作为参数， 用tuple()将list / set转换为元组
from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

choices = ['http:', 'ftp:']
url = 'http://www.python.org'
print(url.startswith(tuple(choices)))

## 切片实现校验
print('=========3===========')
filename = 'spam.txt'
print(filename[-4:] == '.txt')
url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')

## 正则表达式实现
print('=========4===========')
import re
url = 'http://www.python.org'
print(re.match('http:|https:|ftp:', url))






