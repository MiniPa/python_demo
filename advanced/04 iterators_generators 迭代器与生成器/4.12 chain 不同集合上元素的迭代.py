# 不同集合上元素的迭代
## 在多个对象上执行相同的操作，但这些对象在不同的容器中，希望代码在不失可读性情况下避免重复的循环
## itertools.chain() 可用来简化任务，接受一个可迭代对象作为输入，并返回一个迭代器，有效屏蔽在多个
#  容器中的迭代细节

from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)

## 场景1：对不同集合中的所有元素执行某些操作的时候
active_items = set()
inactive_items = set()

for item in chain(active_items, inactive_items):
    '''process item'''
    pass

## itertools.chain() 接受一个或多个可迭代对象作为输入参数，再创建一个迭代器，
#  一次连续的返回每个可迭代对象中的元素，效率高

# Inefficient 
for x in a + b:
    '''会创建一个全新序列，并要求a, b类型一致'''
    pass
# Better
for x in chain(a, b):
    '''chain不会创建全新序列，省略内存'''
    pass



    













































