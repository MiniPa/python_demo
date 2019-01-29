# mmap 内存映射的二进制文件  https://docs.python.org/3/library/mmap.html
## 内存映射一个二进制文件到一个可变字节数组中，目的可能是为了随机访问 它的内容或者是原地做些修改

import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE):
    ''' 内存映射一个二进制文件到一个可变字节数组中 '''
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

# 初始创建一个文件并将其内容扩充到指定大小
print('=========1=========')
size = 1000000
with open('5.10data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

print('=========2=========')
m = memory_map('5.10data')
print(len(m))
print(m[0:10])
print(m[0])
m[0:11] = b'Hello World'
m.close()

# Verify that changes were made
print('=========3=========')
with open('5.10data', 'rb') as f:
    print(f.read(11))

## mmap() 返回的对象 mmap 也可以作为一个上下文管理器来使用，这时候底层文件会被关闭
print('=========4=========')
with memory_map('5.10data') as m:
    print(len(m))
    print(m[0:11])
print(m.closed)

## 默认情况下 memory_map() 函数打开的文件同时支持读和写操作，任何修改的内容都会复制回原来的文件中
filename = '5.10data'
m = memory_map(filename, mmap.ACCESS_READ) # 只读
m = memory_map(filename, mmap.ACCESS_COPY) # 本地修改数据，但不将修改写回原始文件中

## mmap 是一个随机访问文件内容的好方法
#  mmap() 暴露的内存看上去像一个二进制数组对象，但可以用内存视图来解析其中的数据
m = memory_map('5.10data')
v = memoryview(m).cast('I')
v[0] = 7
print(m[0:4])
m[0:4] = b'\x07\x01\x00\x00'
print(v[0])

## 内存映射文件不会导致整个文件被读取到内存中，操作系统仅仅为文件内容保留了一段虚拟内存。
#  当你访问文件不同区域时候，区域的内容才被读并映射到内存区域中，过程透明。
#  多Python解释器内存映射同一个文件,得到的mmap对象能够被用来在解释器，直接交换数据，同时读写，同时生效，要考虑同步问题
























