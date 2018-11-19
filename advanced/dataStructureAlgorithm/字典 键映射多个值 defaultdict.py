# 实现一个键对应多个值的字典（也叫 multidict）
## 将多个值放到另外的容器, 如列表或者集合
d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

## collections.defaultdict 构造字典，会自动初始化每个kye对应的值，只需关注添加元素操作即可
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(1)
d['b'].append(4)
print('====================')
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(1)
d['b'].add(4)
print('====================')
print(d)

## defaultdict会自动为即将访问的key创建映射实体，如果不许要这样的特性，可以在普通的字典上使用setdefault()方法来代替
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('a', []).append(1)
d.setdefault('b', []).append(4)
print('====================')
print(d)

## 自己实现一个多值映射字典 比较麻烦
pairs = '一个迭代对象'
d = {}
for key, value in pairs:
    if key not in d: d[key] = []
d[key].append(value)

d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)