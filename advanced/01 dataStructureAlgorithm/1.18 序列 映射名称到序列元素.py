# 映射名称到序列元素
## 通过下标访问列表/元组中的元素，会使得代码难以阅读
## collections.namedtuple() 本质是一个返回Python中标准元组子类的一个工厂方法，
## 需要传递一个类型名和需要的字段给它，然后返回一个类，可初始化这个类为你定义的字段传值。
from collections import namedtuple

print('==========1==========')
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)

## namedtuple 和元组类型是可交换的，支持所有的普通元组操作
print('==========2==========')
print(len(sub))
addr, joined = sub
print(addr)
print(joined)

## 普通下标版本
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total
## namedtuple 版本
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

## namedtuple 可作为字典的替代，字典需要更多的存储空间
## 构建一个非常大的包含字典的数据结构，使用命名元组更加有效
## namedtuple 是不可更改的
s = Stock('ACME', 100, 123.45)
print(s)
# s.shares = 75
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: can't set attribute

## namedtuple 的 _replace()方法会创建一个全新的命名元组，并将对应值用新值取代
print('==========3==========')
s = s._replace(shares=75)
print(s)

## 创建一个缺省值的原型元组，用_replace()创建值被更新过的实例
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)
def dict_to_stock(s):
    return stock_prototype._replace(**s)
print('==========4==========')
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))

## 如果定义一个需要更新很多实例属性的高效数据结构，namedtuple不是最佳选择
## 可考虑顶一个一个包含 __slots__ 方法的类



















