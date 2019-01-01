# 矩阵与线性代数运算  http://www.numpy.org/
## 如：矩阵乘法、寻找行列式、求解线性方程组

import numpy as np

print('=========1==========')
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
print(m)
print(m.T) # Return transpose
print(m.I) # Return inverse

print('=========2==========')
v = np.matrix([[2],[3],[4]])
print(v)
print(m * v)

print('=========3==========')
## numpy.linalg 中可以找到更多的操作函数
import numpy.linalg
print(numpy.linalg.det(m))  # Determinant
print(numpy.linalg.eigvals(m))  # Eigenvalues

print('=========4==========')
x = numpy.linalg.solve(m, v) # Solve for x in mx = v
print(x)
print(m * x)
print(v)













