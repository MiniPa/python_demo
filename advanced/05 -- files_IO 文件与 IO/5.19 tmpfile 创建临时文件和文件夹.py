# 创建临时文件和文件夹

from tempfile import TemporaryFile

print('=========1=========')
with TemporaryFile('w+t') as f:
    # Read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')

    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()
    print(data)

## 如下方式使用临时文件也是ok的
f = TemporaryFile('w+t')
# Use the temporary file ...
f.close()
# File is destroyed

## TemporaryFile() 支持 w+t w+b
## 也支持和 open() 函数一样的参数
with TemporaryFile('w+t', encoding='utf-8', errors='ignore') as f:
    pass

## 在大多Unix系统上 TemporaryFile() 创建的文件都是匿名的，甚至连目录都没有
## NamedTemporaryFile() 来代替

from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w+t') as f:
    print('filename is:', f.name)

with NamedTemporaryFile('w+t', delete=False) as f:
    '''关闭后、不删除'''
    print('filename is:', f.name)


## 临时目录
from tempfile import TemporaryDirectory

print('=========2=========')
with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)
    # Use the directory
    ...
# Directory and all contents destroyed


## 更低级别的临时目录 mkstemp() mkdtemp(), 但这些函数不会做进一步的管理
# 函数 mkstemp() 仅仅就返回一 个原始的 OS 文件描述符，你需要自己将它转换为一个真正的文件对象，还需要清理这些文件。

import tempfile

print('=========3=========')
tmpfile1 = tempfile.mkstemp()
print(tmpfile1)

tmpfile2 = tempfile.mkdtemp()
print(tmpfile2)

## 一般 临时文件在系统默认位置被创建,如 /var/tmp 或类似的地方
#  可使用 tempfile.gettempdir() 获取真实的位置

print('=========4=========')
tmpdir = tempfile.gettempdir()
print(tmpdir)



































