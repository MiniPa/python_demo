# 迭代器代替 while 无限循环
## 在代码中使用 while 循环来迭代处理数据、因为它需要调用调用某个函数或者和一般迭代模式不同的测试条件
## 可以用迭代器来重写这个循环吗?

## 一常见的IO操作程序
CHUNKSIZE = 8192


def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)


def process_data():
    pass


## 这种代码通常可以使用 iter() 来代替
def reader2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        pass
        # process_data(data)


import sys

f = open('passwd.txt')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)

## iter 它可以接受一个可选的 callable对象和一个标记（结尾）值作为输入参数
## 使用这种方式使用的时候，它会创建一个迭代器，不断调用callable对象直到返回值和标记值相等为止








