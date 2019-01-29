# 编码和解码十六进制数

s = b'hello'

print('=========1=========')
import binascii

## 小小写形式16进制都能处理
h = binascii.b2a_hex(s)
print(h)
s2 = binascii.a2b_hex(h)
print(s2)

import base64

## 只能处理大写形式16进制
h = base64.b16encode(s)
print(h)
s3 = base64.b16decode(h)
print(s3)

## 编码函数所产生的输出总是一个字节字符串，强制使用Unicode输出，需一个额外的界面步骤
h = base64.b16encode(s)
print(h)
print(h.decode('ascii'))

## 解码十六进制时，函数b16decode() 和 a2b_hex() 可接受字节或unicode字符串
#  但是 unicode 字符串必须仅仅只包含 ASCII 编码的十六进制数









































