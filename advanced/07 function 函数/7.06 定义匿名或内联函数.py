# 定义匿名或内联函数

# lambda 表达式
add = lambda x, y: x + y

# 等同于下面函数
def add(x, y):
    return x + y

# lambda 典型场景：排序或数据 reduce 等
names = ['David Beazley', 'Brian Jones','Raymond Hettinger', 'Ned Batchelder']
sorted_names = sorted(names, key=lambda name: name.split()[-1].lower())
print(sorted_names)

# lambda 表达式限制：只能指定 单个表达式，它的值就是最后的返回值
#  不能包含其他的语言特性了，包括多 个语句、条件表达式、迭代以及异常处理等等































