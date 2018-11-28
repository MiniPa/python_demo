# 过滤列元素 利用一些规则数据序列中提取需要的值或者是缩短序列
mylist = [1, 4, -5, 10, -7, 2, 3, -1]

## 使用列表推导
## 缺陷 列表推导在输入非常大的时候会产生一个非常大的结果集，占用大量内存
print('==========1==========')
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

## 使用生成器表达式迭代产生过滤的元素
print('==========2==========')
pos = (n for n in mylist if n > 0)
print(pos)
for x in pos:
    print(x)

## 将过滤代码放入一个函数中，使用内建filter()函数
print('==========3==========')
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

## 1.过滤时候转换数据
print('==========4==========')
import math
print([math.sqrt(n) for n in mylist if n > 0])

## 2.替代型过滤
print('==========5==========')
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)
clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_pos)

## 3.itertools.compress() 多用于用另外一个序列来过滤某个序列
from itertools import compress
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
print('==========6==========')
## 创建一个Boolean序列，指示符合条件的元素，然后compress()函数根据这个序列去选择输出
more5 = [n > 5 for n in counts]
print(more5)
addresses5 = list(compress(addresses, more5))
print(addresses5)


















