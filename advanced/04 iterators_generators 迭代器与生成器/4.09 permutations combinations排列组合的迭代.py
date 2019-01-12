# 排列组合的迭代
## 迭代遍历一个集合中元素的所有可能的排列或组合

## itertools.permutations() 接受一个集合并产生一个元组序列，每个元组由集合中所有元素的一个可能排列组成

items = ['a', 'b', 'c']

from itertools import permutations

print('=========1==========')
for item in permutations(items):
    '''即通过打乱集合中元素排列顺序生成一个元组'''
    print(item)

print('=========2==========')
for item in permutations(items, 2):
    '''传递可选长度参数'''
    print(item)


## itertools.combinations() 得到可输入集合中元素的所有组合
#  对combinations()来说，元素顺序并不重要
from itertools import combinations

print('=========3-1==========')
for c in combinations(items, 3):
    print(c)
print('=========3-2==========')
for c in combinations(items, 2):
    print(c)
print('=========3-3==========')
for c in combinations(items, 1):
    print(c)

## itertools.combinations_with_replacement() 允许同一个元素被选区多次
from itertools import combinations_with_replacement

print('==========4=========')
for c in combinations_with_replacement(items, 3):
    print(c)























