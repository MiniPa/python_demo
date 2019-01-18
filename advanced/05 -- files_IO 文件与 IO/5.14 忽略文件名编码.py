# 忽略文件名编码
## 使用原始文件名执行文件的I/O操作，文件名未经过系统默认编码或解码

# 默认情况下，所有文件名根据如下方法返回文本编码来编码或解码
print(sys.getfilesystemencoding()) # 'utf-8'

# 可以使用一个原始字节字符串来指定一个文件名
# Wrte a file using a unicode filename
with open('jalape\xf1o.txt', 'w') as f:
    f.write('Spicy!')

# Directory listing (decoded)
import os
print(os.listdir('.'))

# Directory listing (raw)
print(os.listdir(b'.'))

# Open file with raw filename
with open(b'jalapen\xcc\x83o.txt') as f:
    print(f.read())

# 后两操作中,给相关文件如 open() 和 os.listdir() 传递字节字符串，文件名处理方式会有所不同

# 有些操作系统允许用户通过偶然或恶意方式去创建名字不符合默认编码的文件,这些文件名可能会神秘地中断那些需要处理大量文件的 Python 程序。
# 读取目录并通过原始未解码方式处理文件名可以有效的避免这样的问题，尽管这 样会带来一定的编程难度




























