# 字典排序  创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。
## collections.OrderedDict
from collections import OrderedDict

d = OrderedDict()
d['abc'] = 1
d['man'] = 4
d['girl'] = 3
d['boy'] = 2
print('====================')
print(d)
## 迭代操作的时候它会保持元素被插入时的顺序
## Outputs: OrderedDict([('abc', 1), ('man', 4), ('girl', 3), ('boy', 2)])

## 用途：如构造一个将来需要序列化或编码成其他格式的映射的时候，如精确控制以JSON编码后字段的顺序
import json
json.dumps(d)

## 1.OrderedDict 内部维护着一个根据插入顺序排序的双向链表，当一个新元素插入时候，被放到链表尾部
## 对于一个已经存在的键的重复赋值不会改变键的顺序
## 2.OrderedDict 是一个普通字典大小的2倍














