# 5.07读写压缩文件
## gzip bz2 可以容易的处理这些文件

## 写入压缩文件
# gzip compression
import gzip
with gzip.open('5.07.gzip.somefile.gz', 'wt') as f:
    f.write('5.07.gzip.somefile.gz')

# bz2 compression
import bz2
with bz2.open('5.07.bz2.somefile.bz2', 'wt') as f:
    f.write('5.07.bz2.somefile.bz2')


## 读取压缩文件
# gzip compression
import gzip
with gzip.open('5.07.gzip.somefile.gz', 'rt') as f:
    text = f.read()
    print(text)

# bz2 compression
import bz2
with bz2.open('5.07.bz2.somefile.bz2', 'rt') as f:
    text = f.read()
    print(text)

## 不指定模式，默认独写文件就是二进制
# gzip.open() bz2.open() 接受跟内置的open()函数一样的参数，包括encoding, errors, newline等

## compresslevel=5 指定压缩级别, 默认是9最高压缩级别
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)

## gzip.open() 和 bz2.open() 可作用在一个已存在并以二进制模式打开的文件上
#  允许gzip bz2 工作在许多类文件对象上，如套接字、管道、内存文件等
import gzip
f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()


































