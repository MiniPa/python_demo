# 5.09 读取二进制数据到可变缓冲区中
## 直接读取二进制数据到一个可变缓冲区中,而不需要做任何的中间复制操作
## 原地修改数据并将它写回到一个文件中去

import os.path

print('=========1=========')
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

# Write a sample file
with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')

buf = read_into_buffer('sample.bin')
print(buf)

buf[0:5] = b'Hallo'
print(buf)

with open('newsample.bin', 'wb') as f:
    f.write(buf)

## 文件对象的 readinto() 方法能被用来为预先分配内存的数组填充数据，甚至包括 由 array 模块或 numpy 库创建的数组
## 和一般read()方法不同，readinto() 填充已存在的缓冲区而不是为新对象重新分配内存再返回它们
## 可以用 readinto() 来避免大量的内存分配操作

print('=========2=========')

record_size = 32 # Size of each record (adjust value)
buf = bytearray(record_size)
with open('somefile.txt', 'rb') as f:
    while True:
        n = f.readinto(buf)
        if n < record_size:
            break
        # Use the contents of buf

## memoryview 可以通过零复制的方式对已存在的缓冲 区执行切片操作，甚至还能修改它的内容
print('=========3=========')
print(buf)
m1 = memoryview(buf)
m2 = m1[-5:]
print(m2)
m2[:] = b'WORLD'
print(buf)

## f.readinto() 时需要注意的是，你必须检查它的返回值，也就是实际读取的 字节数
#  如果字节数小于缓冲区大小，表明数据被截断或者被破坏了 (比如你期望每次读取 指定数量的字节)
#  心观察其他函数库和模块中和 into 相关的函数(比如 recv_into() ， pack_into() 等)
#  Python 的很多其他部分已经能支持直接的 I/O 或数据访问操作，这 些操作可被用来填充或修改数组和缓冲区内容






























