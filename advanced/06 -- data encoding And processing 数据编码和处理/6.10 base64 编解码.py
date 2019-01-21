# 编码解码 Base64 数据

s = b'hello'

import base64

print('=========1=========')
a = base64.b64encode(s)
print(a)

b = base64.b64decode(a)
print(b)

print('=========2=========')
## Base64 编码仅仅用于面向字节的数据，如字节字符串或字节数组，编码处理的输出结果总是一个字节字符串
#  混合使用 Base64 编码的数据和 Unicode 文本，你必须添加一个额外的解码步骤

a = base64.b64encode(s).decode('ascii')
print(a)

## 当解码Base64的时候，字节字符串和Unicode文本都可以作为参数，但是Unicode字符串只能包含 ASCII 字符
















