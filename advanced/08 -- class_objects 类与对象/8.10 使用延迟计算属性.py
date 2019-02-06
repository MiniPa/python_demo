# 使用延迟计算属性

print('=========1=========')
# 将一个只读属性定义成一个 property，第一次被访问计算结果值，并缓存，供后续访问使用
class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius

c = Circle(1.0)
print(c.radius)
print(c.area)
print(c.perimeter)
print(c.area)
print(c.perimeter)
#  消息 Computing area 和 Computing perimeter 仅仅出现一次

## 当一个描述器被放入一个类的定义时，每次访问属性时它的 __get__() 、__set__() 和 __delete__() 方法就会被触发
#  如果一个描述器仅仅只定义了一个 __get__() 方法的话，它比通常的具有更弱的绑定
#  只有当被访问属性不在实例底层的字典中时 __get__() 方法才会被触发

## lazyproperty 类利用这一点，使用 __get__() 方法在实例中存储计算出来的值， 这个实例使用相同的名字作为它的 property。
#  这样一来，结果值被存储在实例字典中并 且以后就不需要再去计算这个 property 了

c = Circle(4.0)
# Get instance variables
print(vars(c)) # {'radius': 4.0}

# Compute area and observe variables afterward
print(c.area) # Computing area 50.26548245743669
print(vars(c)) # {'area': 50.26548245743669, 'radius': 4.0}

# Notice access doesn't invoke property anymore
print(c.area) # 50.26548245743669

# Delete the variable and see property trigger again
del c.area
print(vars(c)) # {'radius': 4.0}
print(c.area) # Computing area 50.26548245743669

print('=========2=========')
## 方案缺陷：被计算的值创建后是可以修改的
print(c.area) # Computing area 50.26548245743669
c.area = 25
print(c.area) # 25

## 方案解决，如下方案修改已经不被允许了
#  缺点就是所有 get 操作都必须被定向到属性的 getter 函数上去
def lazyproperty(func):
    name = '_lazy_' + func.__name__
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value
        return lazy





























