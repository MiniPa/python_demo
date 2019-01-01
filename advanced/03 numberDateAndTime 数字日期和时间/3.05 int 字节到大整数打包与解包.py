# 字节字符串 ~ 大整数
# 如下是16元素 128位长的字节字符串
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

print('=========1===========')
print(len(data))
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))


# 大整数 ~ 字节字符串
print('=========2===========')
x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

## 此操作常见于密码学或网络 IPv6 网络地址是一个128位的整数

## struct 解压字节亦可，不过对于整数大小有限制，可以多次解压，然后合并为最终结果
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
import struct
hi, lo = struct.unpack('>QQ', data)
print((hi << 64) + lo)

## 字节顺序规则 'big' 'little' 仅仅指定了构建整数时的字节低位高位排列方式
x = 0x01020304
print(x.to_bytes(4, 'big'))
print(x.to_bytes(4, 'little'))

## 若果尝试将一个整数打包为字节字符串，那么它就不合适了，会得到一个错误
# 可以用 int.bit_length() 方法决定需要多少字节位来存储这个值
print('=========3===========')
x = 523 ** 23
print(x)
# print(x.to_bytes(16, 'little')) # OverflowError: int too big to convert
print(x.bit_length()) # 208

nbytes, rem = divmod(x.bit_length(), 8)
if rem:
    nbytes += 1
print(x.to_bytes(nbytes, 'little'))






