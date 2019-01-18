# 获取文件夹中的文件列表

import os

names = os.listdir('somedir') # 返回文件列表，包括文件、子目录、符号链接等等

## 过滤某些数据
print('=========1=========')

#  get all regular files
names = [name for name in os.listdir('somedir') if os.path.isfile(os.path.join('somedir', name))]
#   get all dirs
dirnames = [name for name in os.listdir('somedir') if os.path.isdir(os.path.join('somedir', name))]
#  字符串过滤一个目录的内容
pyfiles = [name for name in os.listdir('somedir') if name.endswith('.py')]

#  文件名匹配 glob / fnmatch
import glob
pyfiles = glob.glob('somedir/*.py')

from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('somedir') if fnmatch(name, '*.py')]

## 获取目录中元素的其他元信息，如文件大小、修改时间等等
import os
import os.path
import glob

pyfiles = glob.glob('*.py')

# Get file sizes and modification dates
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name)) for name in pyfiles]
for name, size, mtime in name_sz_date:
    print(name, size, mtime)

# Alternative: Get file metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)






















