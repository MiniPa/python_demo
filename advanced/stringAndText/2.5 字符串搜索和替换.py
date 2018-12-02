# 字符串搜索和替换
print('=========1=========')
text = 'yeah, but no, but yeah, but no, but yeah'
text2 = text.replace('yeah', 'yep')
print('text', ':', text)
print('text2', ':', text2)

## 复杂模式 re.sub()
print('=========2=========')
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
## '\3' 指向前面模式的捕获组号
text2 = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print('text', ':', text)
print('text2', ':', text2)

### 预先编译 提升性能
print('=========3=========')
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
text3 = datepat.sub(r'\3-\1-\2', text)
print('text3')

## 传递一个替换回调函数来代替
print('=========4=========')
from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
print(datepat.sub(change_date, text))

## 替换回调函数的参数是一个match对象，即match()或find()返回的对象。
## 使用group()提取特定的匹配部分，回调函数最后返回替换字符串

## 看一共替换了多少
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)
print(n)









