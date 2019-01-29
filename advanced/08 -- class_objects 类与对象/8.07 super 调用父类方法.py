# 调用父类方法

print('=========1=========')
## 在子类中调用父类的某个已经被覆盖的方法
class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam() # Call parent spam()

## super() 函数的一个常见用法是在 __init__() 方法中确保父类被正确的初始化了
class A:
    def __init__(self):
        self.x = 0

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1

## super() 的另外一个常见用法出现在覆盖 Python 特殊方法的代码中
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value) # Call original __setattr__
        else:
            setattr(self._obj, name, value)

print('=========2=========')
## 直接调用父类的方法，在python中涉及多继承的代码中就可能导致奇怪的问题发生
class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')

class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('B.__init__')

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C.__init__')
#  运行这段代码就会发现 Base.__init__() 被调用两次
c = C()
# Base.__init__
# A.__init__
# Base.__init__
# B.__init__
# C.__init__
## 调用两次不一定会有坏影响，但可以通过super()改进

class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')

class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')

class C(A,B):
    def __init__(self):
        super().__init__() # Only one call to super() here
        print('C.__init__')
#  __init__()只被调用一次了
c = C()
# Base.__init__
# B.__init__
# A.__init__
# C.__init__

## 请读 base/inherit 继承.py python 继承原理

print('=========3=========')
## super() 有个令人吃惊的地方是它并不一定去查找某个类在 MRO 中下一个直接 父类，你甚至可以在一个没有直接父类的类中使用它
class A:
    def spam(self):
        print('A.spam')
        super().spam()

a = A()
# a.spam() # AttributeError: 'super' object has no attribute 'spam'

## 使用多继承看看会发生什么
class B:
    def spam(self):
        print('B.spam')

class C(A,B):
    pass

c = C()
c.spam()
# A.spam
# B.spam

# 在类 A 中使用 super().spam() 实际上调用的是跟类 A 毫无关系的类 B 中的 spam() 方法。
# 这个用类 C 的 MRO 列表就可以完全解释清楚了
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

print('=========4=========')
## 由于 super() 可能会调用不是你想要的方法，你应该遵循一些通用原则
#  4.1：首先，确保在继承体系中所有相同名字的方法拥有可兼容的参数签名 (比如相同的参数个 数和参数名称)
#       可以确保 super() 调用一个非直接父类方法时不会出错
#  4.2: 其次，最好确保最顶层的类提供了这个方法的实现，这样的话在 MRO 上面的查找链肯定可以找到某个确定的方法

## http://rhettinger.wordpress.com/2011/05/26/super-considered-super






































