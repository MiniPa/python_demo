# 使用生成器创建新的迭代模式 -- yield 生成器

## 实现一个自定义的迭代模式，跟普通的内置函数比如 range(), reversed() 不同

def frange(start, stop, increment):
    '''生成一个范围内浮点数的生成器'''
    x = start
    while x < stop:
        yield x
        x += increment

## 使用for循环迭代这个函数，或使用其他接受一个可迭代对象的函数
#  如 sum(), list()等

for f in frange(0, 4, 0.5):
    print(f)

print(list(frange(0, 4, 0.5)))

## 生成器 只能用于迭代操作
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

# Create the generator, notice no output appears
c = countdown(3)
print(c) # <generator object countdown at 0x1006a0af0>

# Run to first yield and emit a value
next(c) # 3
next(c) # 2
next(c) # 1
next(c) # StopIteration

































