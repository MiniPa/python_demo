# 创建新的类或实例属性

print('=========1=========')
# Descriptor attribute for an integer type-checked attribute

class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

## 1.描述器就是一个实现了三个核心的属性访问操作 (get, set, delete) 的类
#  分别 为 __get__() 、__set__() 和 __delete__()
#  这些方法接受一个实例作为输入，之后相应的操作实例底层的字典

## 2.使用一个描述器，需将这个描述器的实例作为类属性放到一个类的定义中

class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

## 所有对描述器属性 (比如 x 或 y) 的访问会被 __get__()、__set__() 和 __delete__() 方法捕获到

p = Point(2, 3)
print(p.x) # Calls Point.x.__get__(p,Point)
p.y = 5 # Calls Point.y.__set__(p, 5)

## 3.作为输入，描述器的每一个方法会接受一个操作实例
#  为了实现请求操作，会相应 的操作实例底层的字典 (__dict__ 属性)
#  描述器的 self.name 属性存储了在实例字 典中被实际使用到的 key

## 4.描述器可实现大部分Python类特性中的底层魔法
#  包括 @classmethod、@staticmethod、@property，甚至是 __slots__ 特性

## 5.通过定义一个描述器，你可以在底层捕获核心的实例操作 (get, set, delete)，并且 可完全自定义它们的行为

## 6.描述器只能在类级别被定义，而不能为每个实例单独 定义
# Does NOT work
class Point:
    def __init__(self, x, y):
        self.x = Integer('x') # No! Must be a class variable
        self.y = Integer('y')
        self.x = x
        self.y = y

## __get__() 看上去有点复杂的原因归结于实例变量和类变量的不同
#  一个描述 器被当做一个类变量来访问，那么 instance 参数被设置成 None。
#  这种情况下，标准做 法就是简单的返回这个描述器本身即可 (尽管你还可以添加其他的自定义操作)
# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

p = Point(2,3)
p.x # Calls Point.x.__get__(p, Point)
Point.x # Calls Point.x.__get__(None, Point)
#  <__main__.Integer object at 0x100671890>

print('=========2=========')
## 基于描述器的代码，并涉及到一个 类装饰器
# Descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

# Class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
        # Attach a Typed descriptor to the class
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate

# Example use
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
## property -- 简单的自定义某个类的单个属性访问的话
## decorate -- 程序中有很多重复代码的时候,在你代码的很多地方使用描述器提供的功能或者将它作为一个函数库特性
























