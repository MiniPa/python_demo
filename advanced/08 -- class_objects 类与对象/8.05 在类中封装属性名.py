# 在类中封装属性名
## Python 程序员不去依赖语言特性去封装数据，而是通过遵循一定的属性和方法命 名规约来达到这个效果。

# 1.任何以单下划线 _ 开头的名字都应该是内部实现
## 下划线开头的约定同样适用于模块名和模块级别函数
class A:
    def __init__(self):
        self._internal = 0 # An internal attribute
        self.public = 1 # A public attribute

    def public_method(self):
        '''
        A public method
        '''
        pass

    def _internal_method(self):
        pass

#  2.使用双下划线开始会导致访问名称变成其他形式
## 下面的类 B 中，私有属性会被分别重命名为 _B__private 和 _B__private_method
## 这种属性通过继承是无法被覆盖的

class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        pass

    def public_method(self):
        pass
        self.__private_method()

class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1 # Does not override B.__private

    # Does not override B.__private_method()
    def __private_method(self):
        pass

## 这里，私有名称 __private 和 __private_method 被重命名为 _C__private 和 _C__private_method ，
#  这个跟父类 B 中的名称是完全不同的。

# 3.大多数而言，你应该让你的非公共名称以单下划线开头
##  代码会涉及到子类，并且有些内部属性应该在子类中隐藏起来，那么才考虑使用双下划线方案

# 4.定义的一个变量和某个保留关键字冲突，这时候可以使用单下划线作为后缀
lambda_ = 2.0 # Trailing _ to avoid clash with lambda keyword
















