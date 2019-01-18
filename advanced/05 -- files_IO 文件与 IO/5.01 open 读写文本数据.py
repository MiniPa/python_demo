# 独写不同编码的文本数据，如 ASCII、UTF-8、UTF-16 编码等

print('=========1-1==========')
with open('somefile.txt', 'rt') as f:
    '''Read the entire file as a single string'''
    data = f.read()
    print(data)

print('=========1-2=========')
with open('somefile.txt', 'rt') as f:
    for line in f:
        '''process line'''
        print(line, end='')
        pass

print('=========2==========')
text1 = 'text1 line'
text2 = 'text2 line'
with open('somefileout1.txt', 'wt') as f:
    '''Write chunks of text 5.10data'''
    f.write(text1)
    f.write(text2)

line1 = 'line1 line'
line2 = 'line2 line'
with open('somefileout2.txt', 'wt') as f:
    print(line1, file=f)
    print(line2, file=f)

print('=========3==========')
with open('somefile.txt', 'rt', encoding='latin-1') as f:
    print(f.read())
    pass

## python 支持非常多的文本编码，ascii, latin-1, utf-8 和 utf-16
#  web 应用程序中通常都使用的是 UTF-8
#  ascii 对应从 U+0000 到 U+007F 范围内 的 7 位字符
#  latin-1 是字节 0-255 到 U+0000 至 U+00FF 范围内 Unicode 字符的直 接映射
## 当读取一个未知编码的文本时使用 latin-1 编码永远不会产生解码错误。
#  使用 latin-1 编码读取一个文件的时候也许不能产生完全正确的文本解码数据，但是它也能 从中提取出足够多的有用数据。
# 同时，如果你之后将数据回写回去，原先的数据还是会 保留的。

## 没有with 就必须手动关闭打开的文件
f = open('somefile.txt', 'rt')
data = f.read()
f.close()

## 换行符 Unix: \n 、 Windows: \r\n
#  默认情况下Python 会读取文本时候，会将普通换行符统一换成 \n, 输出时候再统一换回去
#  可手动指定参数

print('=========4=========')
with open('somefile.txt', 'rt', newline='') as f:
    for line in f:
        print(line, end='')

## 如指定编码格式不正确、可传递errors参数处理错误
print('=========5=========')
# Replace bad chars with Unicode U+fffd replacement char
f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
f.read() ## 'Spicy Jalape?o!'

# Ignore bad chars entirely
g = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
g.read() ## 'Spicy Jalapeo!'





















