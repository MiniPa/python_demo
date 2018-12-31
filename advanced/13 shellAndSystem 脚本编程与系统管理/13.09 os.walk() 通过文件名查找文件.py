# 通过文件名查找文件
import os
import sys

def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))

if __name__ == '__main__':
    findfile(sys.argv[1], sys.argv[2])

## os.walk() 遍历目录树，每进入一个目录，返回一个三元组，包含相对于查找目录的路径，
## 一个该目录下的目录名列表，以及那个目录名下的文件名列表。

## 跨平台，可扩展
import os
import time

# os. path.join() 合并路径
# os.path.abspath() , 它接受一个路径，可能是相对路径，最后返回绝对路径
# os.path.normpath() ，用来返回正常路径，可以解决双 斜杆、对目录的多重引用的问题等
def modified_within(top, seconds):
    '''打印所有最近被修改过的文件'''
    now = time.time()
    for path, dirs, files in os.walk(top):
        for name in files:
            fullpath = os.path.join(path, name)
            if os.path.exists(fullpath):
                 mtime = os.path.getmtime(fullpath)
                 if mtime > (now - seconds):
                    print(fullpath)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Usage: {} dir seconds'.format(sys.argv[0]))
        raise SystemExit(1)
    modified_within(sys.argv[1], float(sys.argv[2]))












