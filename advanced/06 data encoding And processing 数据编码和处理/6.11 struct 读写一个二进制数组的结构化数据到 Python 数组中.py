# 读写一个二进制数组的结构化数据到 Python 元组中

from struct import Struct

print('=========1=========')
def write_records(records, format, f):
    '''
    Write a sequence of tuples to a binary file of structures.
    :param records:
    :param format:
    :param f:
    :return:
    '''
    record_struct = Struct(format)
    for record in records:
        f.write(record_struct.pack(*record))

if __name__ == '__main__':
    records = [ (1, 2.3, 4.5), (6, 7.8, 9.0), (12, 13.4, 56.7) ]
    with open('6.11 data.b', 'wb') as f:
        write_records(records, '<idd', f)

print('=========2=========')
## 很多种方法来读取这个文件并返回一个元组列表

from struct import Struct

def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)

if __name__ == '__main__':
    with open('6.11 data.b','rb') as f:
        for rec in read_records('<idd', f):
            pass
            # Process rec

print('=========3=========')
from struct import Struct

def unpack_records(format, data):
    '''
    将整个文件一次性读取到一个字节字符串中，然后分片解析
    :param format:
    :param data:
    :return:
    '''
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset)
            for offset in range(0, len(data), record_struct.size))

# Example
if __name__ == '__main__':
    with open('data.b', 'rb') as f:
        data = f.read()
    for rec in unpack_records('<idd', data):
        pass
        # Process rec
## 结果都是一个可返回用来创建该文件的原始元组的可迭代对象

# 结构体通常会使用一些结构码值 i, d, f 等, 分别代表某个特定的二进制数据类型如 int32 float64 float32
# Python文档 https://docs.python.org/3/library/struct.html
# "<" 指定了字节顺序，这个例子中表示"低位在前"， ">"表示高位在前，或者是!表示网络字节顺序

## Struct 实例有很多属性和方法用来操作相应类型的结构
#  size 属性包含 了结构的字节数，这在 I/O 操作时非常有用。
#  pack() 和 unpack() 方法被用来打包和 解包数据。

from struct import Struct

record_struct = Struct('<idd')
print(record_struct.size)
record_pack = record_struct.pack(1, 2.0, 3.0)
print(record_pack)
record_struct.unpack(record_pack)

print('=========4=========')
# pack() 和 unpack() 操作以模块级别函数被调用

import struct

pack_struct = struct.pack('<idd', 1, 2.0, 3.0)
print(struct.unpack('<idd', pack_struct))

## 这种方法不优雅，通过一个Struct实例，格式代码只会指定一次并且所有的操作被集中处理


print('=========5=========')
## 如下 iter() 被用来创建并返回一个固定大小数据块的迭代器，
#  这个迭代器会不断的调用一个用户提供的可调用对象，
#  (比如 lambda: f. read(record_struct.size) )，直到它返回一个特殊的值 (如 b’‘)，这时候迭代停止

f = open('6.11 data.b', 'rb')
chunks = iter(lambda: f.read(20), b'')
print(chunks) # <callable_iterator object at 0x10069e6d0>
for chk in chunks:
    print(chk)

## 不使用迭代器，代码会如下
def read_records(format, f):
    record_struct = Struct(format)
    while True:
        chk = f.read(record_struct.size)
        if chk == b'':
            break
        yield record_struct.unpack(chk)

print('=========6=========')
# unpack_records() 中使用了另一种方法 unpack_from()
# unpack_from() 不会产生任何临时对象或者进行内存复制操作，对从大型二进制数组中提取二进制数据非常有用
# 使用 unpack() 代替 unpack_from() 需要修改代码来构造大量的小切片以及进行偏移量的计算 如下:

def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack(data[offset:offset + record_struct.size])
            for offset in range(0, len(data), record_struct.size))
## 这种方案除了看上去很复杂，还得做很多额外工作，它执行了大量的偏移量计算，复制数据以及构造小的切片对象

print('=========7=========')
## 解包时候 namedTuple 可以让你给返回的元组设置属性名称
from collections import namedtuple

Record = namedtuple('Record', ['kind', 'x', 'y'])

with open('6.11 data.b', 'rb') as f:
    records = (Record(*r) for r in read_records('<idd', f))

for record in records:
    print(record.kind, record.x, record.y)

print('=========8=========')
## 如果程序使用大量二进制数据，最好使用 numpy 模块
import numpy as np

f = open('6.11 data.b', 'rb')

records = np.fromfile(f, dtype='<i,<d,<d')
print(records)
print(records[0])
print(records[1])

print('=========9=========')
## 提醒一点，不必要重复造轮子































