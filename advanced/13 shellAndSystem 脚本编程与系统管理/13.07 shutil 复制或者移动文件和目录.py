# 复制或者移动文件和目录

import shutil

src = 'src'
dst = 'dst'

## Copy src to dst. (cp src dst)
shutil.copy(src, dst)
## Copy files, but preserve metadata (cp -p src dst)
shutil.copy2(src, dst)
## Copy directory tree (cp -R src dst)
shutil.copytree(src, dst)
# Move src to dst (mv src dst)
## shutil.move(src, dst)

## default 对于符号链接，这些命令处理的是它指向的东西
## 保留符号链接
shutil.copytree(src, dst, symlinks=True)

## 忽略文件或目录
def ignore_pyc_files(dirname, filenames):
    return
    # return [name in filenames if name.endswith('.pyc')]

shutil.copytree(src, dst, ignore=ignore_pyc_files)
shutil.copytree(src, dst, ignore=shutil.ignore_patterns('*~', '*.pyc'))

## 对于文件元数据信息
## copy2() 访问时间、创建时间和权限这些基本信息 会被保留
##         对于所有者、ACLs、资源 fork 和其他更深层次的文件元信息就说不准 了，这个还得依赖于底层操作系统类型和用户所拥有的访问权限
## 一般不会使用 shutil.copytree()来执行系统备份
## 处理文件名最好用 os.path 中的函数确保最大的可移植性

filename = '/Users/guido/programs/spam.py'

import os.path

os.path.basename(filename) # 'spam.py'
os.path.dirname(filename) # '/Users/guido/programs'
os.path.split(filename) # ('/Users/guido/programs', 'spam.py')
os.path.join('/new/dir', os.path.basename(filename)) # '/new/dir/spam.py'
os.path.expanduser('~/guido/programs/spam.py') # '/Users/guido/programs/spam.py'

## copytree() 碰到异常会被收集到一个列表中并打包成单独的异常
try:
    shutil.copytree(src, dst)
except shutil.Error as e:
    for src, dst, msg in e.args[0]: # src is source name
        # dst is destination name
        # msg is error message from exception
        print(dst, src, msg)








