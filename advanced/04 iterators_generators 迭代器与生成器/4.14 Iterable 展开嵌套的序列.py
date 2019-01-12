# 将一个多层嵌套的序列展开成一个单层的列表

## 写一个包含 yield from 语句的递归生成器来轻松解决这个问题
from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for item in items:
        if isinstance(item, Iterable) and not isinstance(item, ignore_types):
            yield from flatten(item)
        else:
            yield item

items = [1, 2, [3, 4, [5, 6], 7], 8]
for item in flatten(items):
    print(item)

## 上述代码中， isinstance(x, Iterable) 检查某个元素是否是可迭代的
#  是的话，yield from 会返回所有子例程的值，最终返回结果就是一个没有嵌套的简单序列
#  额外参数 ignore_types 和 检测语句 isinstance(x, ignore_types) 用来将字符串和字节排除在迭代对象外
#  防止他们再展开成单个的字符，最终返回我们期望的结果

items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for item in flatten(items):
    print(item)

## yield from 在你想在生成器中调用其他生成器作为子例程的时候非常有用，不使用它的话，就必须写额外的for循环
def flatten(items, ignore_types=(str, bytes)):
    for item in items:
        if isinstance(item, Iterable) and not isinstance(item, ignore_types):
            for i in flatten(item):
                yield i
        else:
            yield item

## yield from 在涉及到基于协程和生成器的并发编程中扮演更加重要的角色



















