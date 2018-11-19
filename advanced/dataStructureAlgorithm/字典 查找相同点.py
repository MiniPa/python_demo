# 字典 查找相同点

a = {
    'x' : 1, 'y' : 2, 'z' : 3
}
b = {
    'w' : 10, 'x' : 11, 'y' : 2
}

## 执行集合操作
print('=========1===========')
# Find keys in common
print(a.keys() & b.keys()) # { 'x', 'y' }
# Find keys in a that are not in b
print(a.keys() - b.keys()) # { 'z' }
# Find (key,value) pairs in common
print(a.items() & b.items()) # { ('y', 2) }

## 以现有字典构造一个排除几个指定键的新字典， 字典推导
print('==========2==========')
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)

## 字典 = key集合 + value集合 的映射关系
## keys() 键视图也支持集合操作，如交、并、差运算 items() 亦同
## values() 值视图不能保证所有值互不相同，会导致某些操作出现问题

















