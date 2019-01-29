# 5.04 读写字节数据

print('=========1=========')
with open('5.04somefile.txt', 'rb') as f:
    data = f.read()
    print(data)
    ## b'1\r\n22\r\n333python\r\n4444\r\n55555python\r\n'

with open('5.04somefileout.bin', 'wb') as f:
    f.write(b'Hello world')
    ## 写入二进制时候，必须保证参数以字节形式对外暴露数据对象(如字节字符串、字节数组对象)

## 读取二进制数据时候，注意区分字节字符串 和 文本字符串，索引和迭代动作返回的是字节的值，而不是字节字符串
print('=========2=========')
t = 'Hello World'
print(t[0])
for c in t:
    print(c)

b = b'Hello World'
print(b[0])
for c in b:
    print(c)

## 从二进制模式的文件中读取或写入文本数据，必须确保要进行节码和编码操作
print('=========3==========')
with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))

## 二进制I/O, 数组和C结构体类型能直接被写入，而无需中间转换为自己对象
print('=========4=========')
import array
nums = array.array('i', [1,2,3,4])
with open('5.04data.bin', 'wb') as f:
    f.write(nums)
#  这个适用于任何实现了"缓冲接口"的对象，会直接暴露其底层的内存缓冲区能给它的处理操作
#  二进制的数据写入就是这类操作之一

#  很多对象允许通过使用文件对象的 readinto() 方法直接读取二进制数据到其底层的内存中去，如：
print('=========5=========')
import array
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('5.04dataout.bin', 'rb') as f:
    f.readinto(a)
print(a)
## 这类技术通常和平台相关，而且可能会依赖子长和字节的顺序（高位优先、低位优先）


























