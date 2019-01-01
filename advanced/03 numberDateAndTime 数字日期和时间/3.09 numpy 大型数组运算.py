# 在大数据集 (比如数组或网格) 上面执行计算

## numpy 相比 标准Python数组，它更适合用来做数学运算

# Python lists
print('=========1==========')
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x * 2) # [1, 2, 3, 4, 1, 2, 3, 4]
# print(x + 10) # TypeError: can only concatenate list (not "int") to list
print(x + y) # [1, 2, 3, 4, 5, 6, 7, 8]
print(x)
print(y)

# numpy arrays
print('=========2==========')
import numpy as np

ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)

## 对整个数组所有元素同时执行数学运算，使得作用在整个数组上的函数运算简单又快速
print('=========3==========')
def f(x):
    return 3*x**2 - 2*x + 7
print(f(ax))

# numpy 提供了大量的math中函数的替代
print(np.sqrt(ax))
print(np.cos(ax))

## numpy 底层使用了C或Fortran语言机制分配内存，它们是一个非常大的连续的并由同类型数据
# 组成的内存区域，可以轻松构造一个比普通Python列表大的多的数组
print('=========4==========')
grid = np.zeros(shape=(10000,10000), dtype=float)
print(grid)

## numpy 扩展 Python 列表的索引功能，特别是对于多维数组
print('=========5==========')
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

print(a)
print(a[1])
print(a[:,1])
# Select a subregion and change it
print('=========6==========')
print(a[1:3, 1:3])
a[1:3, 1:3] += 10
print(a)
# [[ 1  2  3  4]
#  [ 5 16 17  8]
#  [ 9 20 21 12]]

print('=========7==========')
# Broadcast a row vector across an operation on all rows
print(a + [100, 101, 102, 103])
# Conditional assignment on an array
print(np.where(a < 10, a, 10))

a = np.array(
    [[ 1, 2, 3, 4],
    [ 5, 16, 17, 8],
    [ 9, 20, 21, 12]])
# Conditional assignment on an array
print('=========8==========')
print(np.where(a < 10, a, 10))

# http://www.numpy.org/












