# 改变对象的字符串显示

print('=========1=========')
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        '''返回实例的代码表现形式，长用来重新构造这个实例'''
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        '''返回字符串，交互器显示的就是这个 print() 或 str()'''
        return '({0.x!s}, {0.y!s})'.format(self)

p = Pair(3, 4)
# >>> p # Pair(3, 4) # __repr__() output
print(p) # (3, 4) # __str__() output
## 格式化代码 {0.x} 对应的是第 1 个参数的 x 属性
print('p is {0!r}'.format(p)) # p is Pair(3, 4) "!r" ==> 用 repr 代替 str
print('p is {0}'.format(p)) # p is (3, 4)

## 1.__repr__() 生成的文本字符串标准做法是需要让 eval(repr(x)) == x 为真
# 如果实在不能这样子做，应该创建一个有用的文本表示，并使用 < 和 > 括起来
f = open('file.dat')
# <_io.TextIOWrapper name='file.dat' mode='r' encoding='UTF-8'>

#3 2.如果 __str__() 没有被定义，那么就会使用 __repr__() 来代替输出

def __repr__(self):
    return 'Pair({0.x!r}, {0.y!r})'.format(self)
def __repr__(self):
    return 'Pair(%r, %r)' % (self.x, self.y)





































