# 在子类中，扩展定义在父类中的 property 的功能

print('=========1=========')
class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")

## 下面的类继承自 Person 并扩展了 name 属性的功能
## 此例中所有 property 方法都被重新定义，在每一个方法中，使用了 super() 来调用父类的实现
class SubPerson(Person):

    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        # 为了委托给之前定义的 setter 方法，需要将控制权传递给之前定义的 name 属性的 __set__() 方法
        # 获取这个 方法的唯一途径是使用类变量而不是实例变量来访问它，所以使用 super(SubPerson, SubPerson)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)

## 使用新类
s = SubPerson('Guido')
s.name
s.name = 'Larry'
# s.name = 42 # TypeError: Expected a string

print('=========2=========')
## 仅仅只想扩展 property 的某一个方法，可如下操作
class SubPerson(Person):

    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name

# 只想修改 setter 方法
class SubPerson(Person):

    @Person.name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

print('=========3=========')
## 在子类中扩展一个 property 可能会引起很多不容以察觉的问题
#  一个 property 其实是 getter、setter 和 deleter 方法的集合，而不是单个方法。
#  因此，当你扩展一 个 property 的时候，你需要先确定你是否要重新定义所有的方法还是说只修改其中某一个

## 只想重定义其中一个方法，那只使用 @property 本身是不够的，如下不能工作
#  setter 函数整个消失了
class SubPerson(Person):
    @property # Doesn't work
    def name(self):
        print('Getting name')
        return super().name

s = SubPerson('Guido') # AttributeError: can't set attribute

## 同之前说过的那样修改代码，方可成功
## 这么写后，property 之前已经定义过的方法会被复制过来，而 getter 函数被替换。 然后它就能按照期望的工作了
class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name

s = SubPerson('Guido')
s.name
s.name = 'Larry'
print(s.name)
s.name = 42 # TypeError: Expected a string

print('=========4=========')
## 如上特别的解决方案中，没办法使用更加通用的方式去替换硬编码的 Person 类名
#  如果你不知道到底是哪个基类定义了 property，那你只能通过重新定义 所有 property 并使用 super() 来将控制权传递给前面的实现
#  上面演示的第一种技术还可以被用来扩展一个描述器

# A descriptor
class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        instance.__dict__[self.name] = value

# A class with a descriptor
class Person:
    name = String('name')

    def __init__(self, name):
        self.name = name

# Extending a descriptor with a property
class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)

# https://bugs.python.org/issue14965











