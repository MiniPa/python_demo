# 字符串的 I/O 操作
## 使用操作类文件对象的程序来操作文本或二进制字符串

import io

## StringIO 用于 text
print('=========1=========')
sio = io.StringIO()
sio.write('Hello World\n')
print('This is a test', file=sio)
print(sio.getvalue())

print('=========2=========')
sio2 = io.StringIO('Hello\nWorld\n')
print(sio2.read(4))
print(sio2.read())

## BytesIO 用于 bytes
print('=========3=========')
sio3 = io.BytesIO()
sio3.write(b'binary data')
sio3.getvalue()
print(sio3)

## StringIO BytesIO 非常有用，可以用来创建一个包含测试数据的类文件对象,这个对象可以传递给某参数未普通文件对象的函数

































