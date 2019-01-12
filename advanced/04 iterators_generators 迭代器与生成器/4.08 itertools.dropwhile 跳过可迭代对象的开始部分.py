'''
    itertools.dropwhile() 传给它一个函数对象和一个可迭代对象，它会返回一个迭代器对象
    丢弃原有序列中直到函数返回False之前的所有元素，然后返回后面所有元素
'''

print('=========1==========')
with open('passwd.txt') as f:
    for line in f:
        print(line)

print('=========2==========')
## 基于测试函数跳过注释行
from itertools import dropwhile

with open('passwd.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line)

print('=========3==========')
## 基于明确的元素个数跳过元素
from itertools import islice

items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)


## dropwhile() 和 islice() 是两帮助函数，为了避免如下的冗余代码
with open('passwd.txt') as f:

    # Skip over initial comments
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break

    # Process remaining lines
    while line:
        # Replace with useful processing
        print(line, end='')
        line = next(f, None)

## 跳过一个可迭代对象的开始部分跟通常的过滤是不同的，如上述代码的第一个部分可能会这样重写
#  这样写除了跳过开始的注释行，也会跳过文件中其他所有注释行
with open('passwd.txt') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')

























