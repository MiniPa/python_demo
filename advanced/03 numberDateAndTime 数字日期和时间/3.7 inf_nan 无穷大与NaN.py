# 无穷大与NaN 创建或测试正无穷、负无穷或 NaN(非数字) 的浮点数

import math

print('=========1===========')
a = float('inf')
b = float('-inf')
c = float('nan')
print(a, b, c)
print(math.isinf(a))
print(math.isnan(c))

## 无穷大在执行数学运算的时候会传播
a = float('inf')
print(a + 45)
print(a * 10)
print(10 / a)

print('=========2===========')
## 有些未定义的操作会返回 nan
a = float('inf')
print(a/a)
b = float('-inf')
print(a + b)

## NaN值会在所有操作中传播，而不会产生异常
c = float('nan')
print(c + 24)
print(c / 2)

## NaN 之间的比较操作会返回 False
c = float('nan')
d = float('nan')
print(c == d) # False
print(c is d) # False

## 测试一个值是NaN唯一安全的方法就是使用 math.isnan()


## fpectl 是平台相关的，针对专家级程序员，可以改变Python默认行为，在返回无穷大或NaN结果的操作中抛出异常













