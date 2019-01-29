# 文件路径名的操作, 使用路径名来获取文件名，目录名，绝对路径等等

import os

print('=========1=========')
path = '/Users/beazley/Data/data.csv'

basename = os.path.basename(path)
print(basename) # 'data.csv'

dirname = os.path.dirname(path)
print(dirname) # '/Users/beazley/Data'

joinname = os.path.join('tmp', 'data', os.path.basename(path))
print(joinname) # 'tmp/data/data.csv'

path = '~/Data/data.csv'
homepath = os.path.expanduser(path)
print(homepath) # '/Users/beazley/Data/data.csv'

splitpath = os.path.splitext(path)
print(splitpath) # ('~/Data/data', '.csv')

## 任何文件名操作，应该使用 os.path 模块


































