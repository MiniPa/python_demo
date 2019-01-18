# 在不关闭一个已经打开的文件的前提下，增加或改变它的Unicode编码

# 给一个以二进制模式打开的文件添加 Unicode 编码/解码方式，可以使用 io.TextIOWrapper() 对象包装它

import urllib.request
import io

print('=========1=========')
u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()
print(text)

# 修改一个已经打开的文本模式的文件的编码方式，可先使用detach()方法，移除掉已经存在的文本编码层，并使用新的编码方式代替

import sys

print('=========2=========')
print(sys.stdout.encoding) # 'UTF-8'
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
print(sys.stdout.encoding) # 'latin-1'

# IO系统由一系列的层次构建而成，试运行下面的文本文件的例子来查看这种层次
print('=========3=========')
f = open('somefile.txt','w')
print(f) # <_io.TextIOWrapper name='sample.txt' mode='w' encoding='UTF-8'>
print(f.buffer) # <_io.BufferedWriter name='sample.txt'>
print(f.buffer.raw) # <_io.FileIO name='sample.txt' mode='wb'>

# io.TextIOWrapper 是一个编码和解码 Unicode 的文本处理层
# io.BufferedWriter 是一个处理二进制数据的带缓冲的 I/O 层
# io.FileIO 是一个表示操作系统底层文件描述符的原始文件
# 增加或改变文本编码会涉及增加或改变最上面的 io.TextIOWrapper 层

## 如下通过访问属性值来直接操作不同层不安全
print('=========4=========')
print(f)
f = io.TextIOWrapper(f.buffer, encoding='latin-1')
print(f)
print(f.write('Hello')) # ValueError: I/O operation on closed file.
## 原因是 f的原始值已经被破坏了，并关闭了底层文件

# detach() 方法会断开文件的最顶层并返回第二层，之后最顶层就没什么用了
# 如下是改变编码的正确方法
f = open('sample.txt', 'w')
print(f) # <_io.TextIOWrapper name='sample.txt' mode='w' encoding='UTF-8'>

b = f.detach()
print(b) #  <_io.BufferedWriter name='sample.txt'>
f.write('hello') # ValueError: underlying buffer has been detached

f = io.TextIOWrapper(b, encoding='latin-1')
print(f) # <_io.TextIOWrapper name='sample.txt' encoding='latin-1'>

## 利用这种技术来改变文件行 处理、错误机制以及文件处理的其他方面
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii', errors='xmlcharrefreplace')
print('Jalape\u00f1o') # Jalape&#241;o
# 注意下最后输出中的非 ASCII 字符 ñ 是如何被 &#241; 取代的














