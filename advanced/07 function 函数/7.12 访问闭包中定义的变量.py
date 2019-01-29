# 访问闭包中定义的变量
## 扩展函数中某个闭包，允许它访问和修改函数的内部变量
## 一般来说，闭包的内部变量对于外界来说都是影藏的，但你可以通过编写访问函数并将其作为函数属性绑定到闭包上实现

print('=========1=========')
def sample():
    n = 0
    # Clousure function
    def func():
        print('n=', n)

    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func

## 使用方式
f = sample()
f() # n=0
f.set_n(10)
f() # n=10
print(f.get_n()) # 10

#  1.nonlocal 声明可以让 我们编写函数来修改内部变量的值
#  2.函数属性允许我们用一种很简单的方式将访 问方法绑定到闭包函数上
#  3.还可以进一步的扩展，让闭包模拟类的实例，要做的仅仅是复制上面的内部函数 到一个字典实例中并返回它即可

print('=========2=========')
import sys

class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
        # Update instance dictionary with callables
        self.__dict__.update(
            (key,value) for key, value in locals.items() if callable(value))

    # Redirect special methods
    def __len__(self):
        return self.__dict__['__len__']()

# Example use
def Stack():
    items = []
    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

## 演示一下
s = Stack()
print(s)
s.push(10)
s.push(20)
s.push('hello')
print(len(s))
print(s.pop())
print(s.pop())
print(s.pop())

print('=========3=========')
## 这个代码运行起来会比一个普通的类定义要快很多，如下是一个性能对比类
class Stack2:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

from timeit import timeit

s = Stack()
timeit('s.push(1);s.pop()', 'from __main__ import s') # 0.9874754269840196
s = Stack2()
timeit('s.push(1);s.pop()', 'from __main__ import s') # 1.0707052160287276

## 闭包方案大概快 8%, 原因是对实例变量的访问简化了，闭包也不会涉及到额外的 self 变量























