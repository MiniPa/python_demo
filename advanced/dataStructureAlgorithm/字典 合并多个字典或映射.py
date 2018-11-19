# 合并多个字典或映射
## 将多个字典或映射从逻辑上合并为单一的映射后执行某些操作，如查找值或检测某些键是否存在

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap
print('==========1==========')
c = ChainMap(a, b)
print(c['x'])
print(c['z'])
## ChainMap 逻辑上的字典，大部分字典操作都是ok的
## 重复键优先选择第一次出现的
## 更新或删除操作，总是影响列表中的第一个字典

c['z'] = 10
c['w'] = 40
del c['x']
print('==========2==========')
print(a)
print(b)

values = ChainMap()
values['x'] = 1

print('==========3==========')
# Add a new mapping
values = values.new_child()
values['x'] = 2

# Add a new mapping
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])

# Discard last mapping
values = values.parents
print(values['x'])

# Discard last mapping
values = values.parents
print(values['x'])
print(values)





















