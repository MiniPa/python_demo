# 测试文件是否存在

import os

print('=========1=========')
print(os.path.exists('/etc/passwd'))
print(os.path.exists('/tmp/spam'))
print(os.path.isfile('/etc/passwd'))
print(os.path.isdir('/etc/passwd'))
print(os.path.islink('/usr/local/bin/python3'))
print(os.path.realpath('/usr/local/bin/python3')) # '/usr/local/bin/python3.3'
print(os.path.getsize('/etc/passwd'))
print(os.path.getmtime('/etc/passwd'))

import time

print(time.ctime(os.path.getmtime('/etc/passwd')))

## 要考虑文件权限问题，特别是在获取元数据的时候
print(os.path.getsize('/Users/guido/Desktop/foo.txt')) # PermissionError


























