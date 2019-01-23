# 减少可调用对象的参数个数
## 有一个被其他 python 代码使用的 callable 对象，可能是一个回调函数或者一个处理器，但参数太多了，导致调用出错

## functools.partial() 给一个或多个参数设置固定值，减少接下来被调用时的参数个数
def spam(a, b, c, d):
    print(a, b, c, d)

from functools import partial

print('=========1=========')
s1 = partial(spam, 1) # a = 1
s1(2, 3, 4)
s1(4, 5, 6)

print('=========2=========')
s2 = partial(spam, d=42) # d = 42
s2(1, 2, 3)
s2(4, 5, 6)

print('=========3=========')
s3 = partial(spam, 1, 2, d=42) # a = 1, b = 2, d = 42
s3(3)
s3(4)

## 让原本不兼容的代码可以一起工作
points = [ (1, 2), (3, 4), (5, 6), (7, 8) ] # (x, y) 代表点

import math

def distance(p1, p2):
    '''计算两点之间的距离'''
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 -x1, y2 - y1)







































