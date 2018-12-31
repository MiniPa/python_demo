# 合并拼接字符串

print('=========1=========')
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

a = 'Is Chicago'
b = 'Not Chicago?'
print('{} {}'.format(a,b))
print(a + ' ' + b)

a = 'Hello' 'World'
print(a)

# '+' 会引起大量内存复制和垃圾回收，下面操作决不允许
print('=========2=========')
s = ''
for p in parts:
    s += p
print(s)

# 利用表达式生成器
print('=========3=========')
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

# 注意不必要的字符串连接操作
a = 'a1'
b = 'b2'
c = 'c3'
print(a + ':' + b + ':' + c) # Ugly
print(':'.join([a, b, c])) # Still ugly
print(a, b, c, sep=':') # Better

# 研究程序选择合适的方式
chunk1 = 'chunk1'
chunk2 = 'chunk2'
with open('out.txt') as f:
    # Version 1 (string concatenation)
    f.write(chunk1 + chunk2)

    # Version 2 (separate I/O operations) f.write(chunk1)
    f.write(chunk2)
## 两短chunk，version1 效果好，反之则 version2 效果好，考虑I/O和内存块等性状

# 构建大量小字符串的输出代码，最好考虑下使用生成器函数
print('=========3=========')
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'
## 生成器函数并没有对输出片段到底要怎样组织做出假设
text = ''.join(sample())
print(text)
## 将字符串重定向到I/O
for part in sample():
    f.write(part)
## 写出一些结合I/O操作的混合方案
def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
        yield ''.join(parts)
## 结合文件操作
with open('filename', 'w') as f:
    for part in combine(sample(), 32768):
        f.write(part)
### 原始的字符串生成器函数并不需要知道使用细节，只负责生成字符串片段即可























