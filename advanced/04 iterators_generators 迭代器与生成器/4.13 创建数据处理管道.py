# 创建数据处理管道

## 以数据管道（类似Unix管道）的方式迭代处理数据

## 假设有一个非常大的日志文件目录
# foo/
#     access-log-012007.gz
#     access-log-022007.gz
#     access-log-032007.gz
#     ...
#     access-log-012008
# bar/
#     access-log-092007.bz2
#     ...
#     access-log-022008

## 日志文件数据
#  124.115.6.12 - - [10/Jul/2012:00:18:50 -0500] "GET /robots.txt ..." 200 71
#  210.212.209.67 - - [10/Jul/2012:00:18:51 -0500] "GET /ply/ ..." 200 11875
#  210.212.209.67 - - [10/Jul/2012:00:18:51 -0500] "GET /favicon.ico ..." 404 369
#  61.135.216.105 - - [10/Jul/2012:00:20:04 -0500] "GET /blog/atom.xml ..." 304

import os
import fnmatch
import gzip
import bz2
import re

## 定义一个由多个执行特定任务独立任务的简单生成器 函数组成的容器
def gen_find(filepat, top):
    '''
    Find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)

def gen_opener(filenames):
    '''
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()

def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators together into a single sequence.
    '''
    for it in iterators:
        yield from it

def gen_grep(pattern, lines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


## 将这些函数连起来创建一个处理管道，如查找包含单词为python的所有日志行
lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
for pyline in pylines:
    print(pyline)

## 将来你想扩容管道、可以在生成器表达式中包装数据，如下面这个版本计算出传输的字节数并计算总和
lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
bytecolumn = (line.rsplit(None, 1)[1] for line in pylines)
bytes = (int(x) for x in bytecolumn if x != '-')
print('Total', sum(bytes))

## 以管道方式处理数据，可以用来解决各类其他问题，包括解析、读取实时数据、定时轮询等
#  yeild 作为数据的产生者
#  for 循环作为数据的消费者
#  这些生成器被连载一起，每个yield会将一个独立的数据元素传递给迭代处理管道的下一阶段
#  此例中 sum() 是程序最终的驱动者，每次从生成器管道中提取一个元素

## 优点：生成器小而独立，易于维护，复用，也比较容易理解
#       内存效率也比较高，只需要很小的内存

## gen_concatenate() 将输入的序列拼接成一个很长的行序列
#  itertools.chain() 具有类似的功能、但需要将所有可迭代对象作为参数传入
#  上面例子如果写作：lines = itertools.chain(*files)，会导致gen_opener()生成器提前被全部消费掉
#  由于gen_opener() 生成器每次生成一个打开过的文件，等到下一个迭代步骤时候文件就关闭了，所以chain()在这里不能这样用
#  上面方案可以避免这种情况

## gen_concatenate() 函数中出现过 yield from 语句，它将 yield 操作代理到父生成器上去。
#  yield from it 简单返回生成器 it 所产生的所有值

































