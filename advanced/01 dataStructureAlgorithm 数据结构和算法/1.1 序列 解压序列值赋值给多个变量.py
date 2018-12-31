# 1.1 解压序列值赋值给多个变量
## 多个变量 = 任何序列(任何可迭代对象：包括字符串、文件对象、迭代器、生成器)
p = (4, 5)
x, y = p

data = ['ACE', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
name, shares, price, (year, mon, day) = data

## 任意变量名去占位
_, shares, price, _ = data



# 1.2 解压可迭代对象赋值给多个变量
## "*" 代表任意个数元素，按位置解压元素
grade = [20, 30, 40, 0, 35, 55, 25]
first, *middle, last = grade

## "*" 在字符串分割时候使用
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
uname, *_, homedir, sh = line.split(':')

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record

## "*" 在迭代元素为可变长元组的序列时是很有用的
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]
def do_foo(x, y): print('foo', x, y)
def do_bar(s): print('bar', s)
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

## "*" 可以用来实现巧妙的递归运算, 递归并非Python擅长，不用太认真研究这个
items = [1, 10, 7, 4, 5, 9]
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
print(sum(items))

















































