# 创建可管理的属性
## 给某个实例 attribute 增加除访问与修改之外的其他处理逻辑，比如类型检查 或合法性验证

print('=========1=========')
# 1.定义一个property，增加对一个属性简单的类型检查
class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

## property 被访问的时候会自动触发 getter、setter、deleter 方法
a = Person('Guido')
print(a.first_name)
# a.first_name = 42 # raise TypeError('Expected a string')
# del a.first_name # AttributeError: can`t delete attribute

# _first_name 是实际数据保存的地方

print('=========2=========')
# 2.在已存在的 get 和 set 方法基础上定义 property
## 在初始化方法中调用setter方法校验

class Person:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    name = property(get_first_name, set_first_name, del_first_name)

print('=========3=========')
# property 属性其实就是一系列相关绑定方法的集合
# 查看拥有 property 的类，就会发现 property 本身的 fget、fset 和 fdel 属性就是类里面的普通方法

print(Person.first_name.fget) # <function Person.first_name at 0x1006a60e0>
print(Person.first_name.fset) # <function Person.first_name at 0x1006a6170>
print(Person.first_name.fdel) # <function Person.first_name at 0x1006a62e0>

## 通常来讲，你不会直接取调用 fget 或者 fset，它们会在访问 property 的时候自动被触发
## 当你确实需要对 attribute 执行其他额外的操作的时候才应该使用到 property

## 有时候一些从其他编程语言 (比如 Java) 过来的程序员总认为所有访问都应该通过 getter 和 setter，
## 所以他们认为代码应该像下面这样写：

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value
## 不要写这种没有做任何其他额外操作的 property
#  1.代码变得很臃 肿，并且还会迷惑阅读者
#  2.让你的程序运行起来变慢很多
#  3.这样的设 计并没有带来任何的好处
#  4.当你以后想给普通 attribute 访问添加额外的处理逻辑的时候，
#    你可以将它变成一个 property 而无需改变原来的代码。因为访问 attribute 的代码还是保持原样

print('=========4=========')
## Properties 还是一种定义动态计算 attribute 的方法,这种类型的 attributes 并不会 被实际的存储，而是在需要的时候计算出来。
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
## 通过使用 properties，将所有的访问接口形式统一起来
#  对半径、直 径、周长和面积的访问都是通过属性访问，就跟访问简单的 attribute 是一样的
#  不这样做的话，那么就要在代码中混合使用简单属性访问和方法调用

c = Circle(4.0)
print(c.radius)
print(c.area) # Notice lack of ()
print(c.perimeter) # Notice lack of ()

print('=========5=========')
## 尽管 properties 可以实现优雅的编程接口，但有些时候你还是会想直接使用 getter 和 setter 函数
p = Person('Guido')
print(p.get_first_name())
print(p.set_first_name('Larry'))
## 这样做原因可能是Python 代码被集成到一个大型基础平台架构或程序中
#  有可能是一个 Python 类准备加入到一个基于远程过程调用的大型分布式系 统中。
#  这种情况下，直接使用 get/set 方法 (普通方法调用) 而不是 property 或许会更 容易兼容

print('=========6=========')
## 不要像下面这样写有大量重复代码的 property 定义
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Repeated property code, but for a different name (bad!) @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._last_name = value
## 代码臃肿，通过使用装饰器或闭包， 有很多种更好的方法来完成同样的事情















