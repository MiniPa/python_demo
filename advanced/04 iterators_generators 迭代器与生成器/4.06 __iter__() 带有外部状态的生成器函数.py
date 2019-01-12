# 定义一个生成器函数，但它会调用某个你想暴漏给用户使用的外部环境

## 如果你想让你的生成器暴露外部状态给用户，可简单将其实现为一个类，然后将生成器函数放到 __iter__() 函数中

from collections import deque

class linehistory:

    def __init__(self, lines, histlen=3) :
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

## 使用这个类，可以将之当作一个普通生成器函数

with open('somefile.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')

## 生成器函数如果需要程序的其他部分打交道，如暴漏属性值、允许通过方法调用来控制
#  可能会导致代码异常复杂
#
#  此时可考虑使用上面介绍的类定义的方式、在__iter__()中定义生成器不会改变算法任何逻辑,
#  此外它是类的一部分，允许你定义各种属性和方法供用户使用

## 注意：迭代中如果不使用for循环语句，你得先调用iter()函数
f = open('somefile.txt')
lines = linehistory(f)
it = iter(lines) # attention
print(next(it))
print(next(it))


















