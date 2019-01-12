# 同时迭代多个序列，每次分别从一个序列中取一个元素

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]

print('=========1==========')
for x, y in zip(xpts, ypts):
    '''一旦某个序列到底结尾，迭代宣告结束，迭代长度和参数中最短序列长度一致'''
    print(x, y)

print('=========2==========')
a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a,b):
    print(i)

from itertools import zip_longest

print('=========3==========')
for i in zip_longest(a, b):
    '''default: None'''
    print(i)

print('=========4==========')
for i in zip_longest(a, b, fillvalue=0):
    '''fill with 0'''
    print(i)


## zip() 将序列打包并生成一个字典
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]

print('=========5==========')
s = dict(zip(headers, values))
for name, val in zip(headers, values):
    print(name, '=', val)

# zip() 可接受多余两个的序列的参数，生成的结果元组中元素的个数跟输入的序列个数一样
print('=========6==========')
a = [1, 2, 3]
b = [10, 11, 12]
c = ['x','y','z']

for i in zip(a, b, c):
    print(i)

## zip() 会创建一个迭代器来作为结果返回，可用list()将结果值存储起来
print('=========7==========')
print(type(zip(a, b)))
print(list(zip(a, b)))


































