# 定义有默认参数的函数

## 方法：给参数指定一个默 认值，并放到参数列表最后
def spam(a, b=42):
    print(a, b)

spam(1) # Ok. a=1, b=42
spam(1, 2) # Ok. a=1, b=2

## 默认参数是一个可修改的容器比如一个列表、集合或者字典，可以使用 None 作为默认值
#  默认参数的值应该是不可变的对象，比如 None、True、False、数字或字符 串
#  这里的 b=None 不能修改为 b = [], 因为 []是可变的，会引起函数使用的混乱
def spam(a, b=None):
    if b is None: ## if not b 是不课去
        b = []

# 测试下某默认参数是不是有值传入
_no_value = object() ## 一个独一无二的私有对象实例，用户不可能传递这个对象进来

def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')

## 默认参数的值仅仅在函数定义的时候赋值一次
x = 4
def spam(a, b=x):
    print(a, b)
spam(1) # 1, 4

x = 2 # 函数在定义的时候就被赋值了，且不会改变
spam(1) # 1, 4













