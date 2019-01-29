# 读写 JSON(JavaScript Object Notation) 编码格式的数据

import json

print('=========1 json 和 str=========')
data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}
json_str = json.dumps(data)
print(json_str)
json_data = json.loads(json_str)
print(json_data)

print('=========2 json 和 file=========')
with open('6.02 data_w.json', 'w') as f:
    json.dump(data, f)

with open('6.02 data_r.json', 'r') as f:
    data = json.load(f)
    print(data)

print('=========3=========')
## JSON 支持的数据类型为 None、bool、int、float、str
#  以及包含这些类型数据的 lists、tuples 和 dictionaries

## 对于 dictionaries keys 需要是 str 类型，其他类型会被先转换成 str
## JSON 编码格式对于Python几乎一样，除 True 映射成 true, False ~ false, None ~ null

print(json.dumps(False)) # 'false'
d = {'a': True, 'b': 'Hello', 'c': None}
print(json.dumps(d)) # '{"b": "Hello", "c": null, "a": true}'

print('=========4=========')
# pprint() 代替普通的 print(), 格式化打印 json

from urllib.request import urlopen
from pprint import pprint
import json

# u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
# resp = json.loads(u.read().decode('utf-8'))
# pprint(resp)

print('=========5=========')
## 一般来说Python会根据提供的数据创建 dicts 或 lists
#  创建其他类型的对象，可以给 json.loads() 传递 object_pairs_hook 或 object_hook 参数

# 解码 JSON 数据并在一个 OrderedDict 中保留其顺序
s = '{"name": "ACME", "shares": 50, "price": 490.1}'

from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)

## 将一个JSON字典转化成 Python对象

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

data = json.loads(s, object_hook=JSONObject)
print(data.name, '-', data.shares, '-', data.price)
print(data)

## json.dumps() 的 indent 参数使得输出效果和 pprint() 一样
print(json.dumps(data)) # {"price": 542.23, "name": "ACME", "shares": 100}
print(json.dumps(data, indent=4))
# {
#     "price": 542.23,
#     "name": "ACME",
#     "shares": 100
# }

print('=========6=========')
## 对象实例通常不可序列化，如下：
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
# json.dumps(p) # TypeError: <__main__.Point object at 0x1006f2650> is not JSON serializable

## 可以提供一个函数，输入是一个实例，返回一个可序列化的字典
def serialize_instance(obj):
    d = { '__classname__' : type(obj).__name__ }
    d.update(vars(obj))
    return d
# 反过来获取实例如下操作
# Dictionary mapping names to known classes
classes = {
    'Point' : Point
}

def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls) # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d

# 使用范例
p = Point(2,3)
s = json.dumps(p, default=serialize_instance)
print(s) # '{"__classname__": "Point", "y": 3, "x": 2}'
a = json.loads(s, object_hook=unserialize_object)
print(a) # <__main__.Point object at 0x1017577d0>
print(a.x, '-', a.y)




















