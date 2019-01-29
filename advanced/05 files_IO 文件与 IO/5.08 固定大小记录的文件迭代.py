# 5.08 固定大小记录的文件迭代
## 想在一个固定长度记录或者数据块的集合上迭代，而不是在一个文件中一行一 行的迭代

from functools import partial

RECORD_SIZE = 32

with open('somefile.txt', 'rb') as f:
    '''
    records 对象是一个可迭代对象，不断产生固定大小数据块，直到文件末尾
    如果总记录大小不是块大小整数备，最后一个返回元素的字节数会比期望值少
    '''
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for record in records:
        print(record)

## 给iter()传递一个可调用对象和一个标记值，它会创建一个迭代器
#  这个迭代器会一直调用传入的可调用对象直到它返回标记值为止，此时迭代终止

## 上述案例 functools.partial 用来创建一个每次被调用时从文件中读取固定数目字节的可调用对象 标记b''就是到达文件结尾
































