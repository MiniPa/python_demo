# 字符串对齐
text = 'Hello World'

print('=========1=========')
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
print(text.center(20, '*'))

print('=========2=========')
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
print(format(text, '=>20s'))
print(format(text, '*^20s'))

print('=========3=========')
a = '{:>10s} {:>10s}'.format('Hello', 'World')
print(a)

# format() 可以用来格式化任何值
print('=========4=========')
x = 1.2345
x1 = format(x, '=>10')
print(x1)
x2 = format(x, '=^10.2f')
print(x2)

# % 操作
print('%-20s' % text)
print('%20s' % text)










