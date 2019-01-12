# 想得到一个由迭代器生成的切片对象，但标准切片操作并不能做到

def count(n):
    while True:
        yield n
        n += 1

c = count(0) # 一个迭代器对象
# print(c[10: 20])

## 使用 itertools.islice() 来做切片操作

import itertools
for x in itertools.islice(c, 10, 20):
    print(x)

## 迭代器和生成器不能使用标准的切片操作，因为我们不清楚它的长度，也没有索引
#  slice()会消耗掉传入迭代器中的数据，必须考虑到迭代器不可逆




    


























