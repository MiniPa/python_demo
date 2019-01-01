# 二、八、十六进制文本

x = 1234

print('=========1===========')
print(bin(x))
print(oct(x))
print(hex(x))

print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

x2 = -1234
print(format(x2, 'b')) # -10011010010
print(format(x2, 'x')) # -4d2

## 产生无符号值
print(format(2**32 + x, 'b')) # 100000000000000000000010011010010
print(format(2**32 + x, 'x')) # 1000004d2

## 以不同进制转换整数字符串、简单的使用带有进制的int()即可
print('=========2===========')
print(int('4d2', 16)) # 1234
print(int('10011010010', 2)) # 1234

## Python 指定8进制和其他语言稍有不同，如下是错误的
import os
# os.chmod('script.py', 0755) # SyntaxError: invalid token
os.chmod('script.py', 0o755)  # 8进制前缀是0o
















