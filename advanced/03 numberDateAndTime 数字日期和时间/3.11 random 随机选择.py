# 随机选择
## 从一个序列中随机抽取若干元素，或者想生成几个随机数。

import random

print('=========1==========')
## 从一个序列中随机元素
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))
print(random.sample(values, 2))

## 打乱序列中元素的顺序
print('=========2==========')
random.shuffle(values)
print(values)

## 生成随机数
print('=========3==========')
print(random.randint(0, 10)) # Integer
print(random.random()) # Float 0 ~ 1

## 获取N位随即位（二进制）的整数
print('=========4==========')
print(random.getrandbits(200))

## random 使用 Mersenne Twister 算法来计算生成随机数，是一个确定性算法
# 但可以通过 random.seed() 函数修改初始化种子
random.seed() # Seed based on system time or os.urandom()
random.seed(12345) # Seed based on integer given
random.seed(b'bytedata') # Seed based on byte 5.10data

## random 还包含基于均匀分布、高斯分布、其他分布的随机数生成函数
# random.uniform() 计算均匀分布随机数
# random.gauss() 计算正太分布随机数

## random 不应用于在和密码学相关的程序中
# 类似功能可以使用 ssl.RAND_bytes() 生成一个安全的随机字节序列











