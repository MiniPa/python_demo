# 复数的数学运算

print('=========1===========')
a = complex(2, 4)
b = 3 - 5j
print(a)
print(b)
print(a.real)
print(a.imag)
print(a.conjugate())

## 常见数学运算皆可
print('=========2===========')
print(a + b)
print(a * b)
print(a / b)
print(abs(a))

## 执行其他的复数函数，如正弦、余弦、平方根 使用cmath模块
print('=========3===========')
import cmath
print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))

## Python中大部分数学模块都可以处理复数

import numpy as np
print('=========4==========')
a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(a)
print(a + 2)
print(np.sin(a))

## Python 标准数学函数一般情况下，不能产生复数值，代码中不能出现复数返回值
import math
# math.sqrt(-1) # ValueError: math domain error
# cmath 模块，或在某支持复数的库中申明复数类型的使用

import cmath
print('=========5==========')
print(cmath.sqrt(-1))























