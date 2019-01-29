# 打印不合法的文件名 UnicodeEncodeError surrogates not allowed

def bad_filename(filename):
    return repr(filename)[1:-1]

filename = ''
try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))

# Python 假定所有文件名都已经根据 sys.getfilesystemencoding() 的值编码过了
# 有一些文件系统并没有强制要求这样做，因此允许创建文件名没 有正确编码的文件
# 总会有些用户冒险这样做或者是无意之 中这样做了

# 不合规范的文件名就会让 Python 陷入困境
# 不能仅仅只是丢弃这些不合格的名字
# 不能将 这些文件名转换为正确的文本字符串
# Python 解决方案：从文件名中获 取未解码的字节值比如 \xhh 并将它映射成 Unicode 字符 \udchh 表示的所谓的”代理 编码”

import os

# 演示了当一个不合格目录列表中含有一个文件名为 bäd.txt(使用 Latin-1 而不是 UTF-8 编码) 时的样子
files = os.listdir('.')
print(files) # ['spam.py', 'b\udce4d.txt', 'foo.txt']

# 有代码需要操作文件名或者将文件名传递给 open() 这样的函数，一切都能 正常工作
# 想要输出文件名时才会碰到些麻烦 (比如打印输出到屏幕或日志文 件等)
# 当你想打印上面的文件名列表时，你的程序就会崩溃

for name in files:
    print(name)
# UnicodeEncodeError
# 崩溃原因：字符 \udce4 是一个非法的 Unicode 字符
# 它其实是一个被 称为代理字符对的双字符组合的后半部分。由于缺少了前半部分，因此它是个非法的 Unicode
# 唯一能成功输出的方法就是当遇到不合法文件名时采取相应的补救措施

for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename(name))

# 在 bad_filename() 函数中如何处置取决于个人，还有就是通过某种方式重新编码
def bad_filename(filename):
    temp = filename.encode(sys.getfilesystemencoding(), errors='→֒surrogateescape')
    return temp.decode('latin-1')

# surrogateescape:
# 这种是 Python 在绝大部分面向 OS 的 API 中所使用的错误处理器，
# 它能以一种优雅的方式处理由操作系统提供的数据的编码问题。
# 在解码出错时会将出错字节存储到一个很少被使用到的 Unicode 编码范围内。 在编码时将那些隐藏值又还原回原先解码失败的字节序列。
# 它不仅对于 OS API 非常有用，也能很容易的处理其他情况下的编码错误。

for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename(name))



































