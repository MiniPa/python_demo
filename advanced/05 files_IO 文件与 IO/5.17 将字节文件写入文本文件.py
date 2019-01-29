# 在文本模式打开的文件中写入原始的字节数据

import sys

print('=========1=========')
## 将字节数据直接写入文件的缓冲区即可
## 能够通过读取文本文件的 buffer 属性来读取二进制数据
sys.stdout.write(b'Hello\n') # TypeError: must be str, not bytes
sys.stdout.buffer.write(b'Hello\n')  # Hello 直接写入缓冲区

## I/O 系统以层级结构的形式构建而成
# 文本文件：通过在一个拥有缓冲的二进制模 式文件上增加一个 Unicode 编码/解码层来创建
#       buffer 属性指向对应的底层文件, 如果你直接访问它的话就会绕过文本编码/解码层













