# 匹配和搜索特定模式的文本
import re

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

print('=========1===========')
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

## 模式对象
print('=========2===========')
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')
if datepat.match(text2):
    print('yes')
else:
    print('no')


## 查找所有
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print('=========3===========')
print(datepat.findall(text))

## regex 利用 () 捕获分组
print('=========4===========')
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m.group(1))
print(m.groups())
print(datepat.findall(text))

for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

## 以迭代形式返回
print('=========5==========')
for m in datepat.finditer(text):
    print(m.groups())

## 精确匹配 $
print('=========6==========')
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(datepat.match('11/27/2012abcdef'))
print(datepat.match('11/27/2012'))

## 直接使用模块级别函数，如下，会缓存最近编译过的模式，并不会损耗太多性能
## 大量的匹配和搜索的话，最好先编译正则表达式
print('=========6==========')
result = re.findall(r'(\d+)/(\d+)/(\d+)', text)
print(result)





