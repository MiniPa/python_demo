# inherit python 继承的原理

## 1.每一个类，Python 会计算出一个所谓的方法解析顺序 (MRO) 列表
#    MRO 列表就是一个简单的所有基类的线性顺序表

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

## Base MRO
# (
# <class '__main__.C'>,
# <class '__main__.A'>,
# <class '__main__.B'>,
# <class '__main__.Base'>,
# <class 'object'>
# )

## 2.为了实现继承，Python 会在 MRO 列表上从左到右开始查找基类，直到找到第一 个匹配这个属性的类为止
## 3.MRO 列表的构造是通过一个 C3 线性化算法来实现的,实际上就是合并所有父类的 MRO 列表并遵循如下三条准则

#  3.1: 子类会先于父类被检查
#  3.2: 多个父类会根据它们在列表中的顺序被检查
#  3.3: 如果对下一个类存在两个合法的选择，选择第一个父类

## 4.MRO 列表中的类顺序会让你定义的任意类层级关系 变得有意义
#  使用 super() 函数时，Python 会在 MRO 列表上继续搜索下一个类

#  只要 每个重定义的方法统一使用 super() 并只调用它一次，
#  那么控制流最终会遍历完整个 MRO 列表，每个方法也只会被调用一次
#  这也是为什么在第二个例子中你不会调用两 次 Base.__init__() 的原因
































