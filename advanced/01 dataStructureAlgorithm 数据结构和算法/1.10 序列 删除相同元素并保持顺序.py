# 删除序列相同元素并保持顺序
## 序列上都是 hashable值, 可以简单的利用集合或者生成器来解决这个问题
print('==========1==========')
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))

## 序列元素不可hashable
print('==========2==========')
def dedupe(items, key=None):
    seen = set()
    for item in items:
        ## key 参数指定一函数将元素转变成hashable
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe(a, key=lambda d: d['x'])))

## 构造简单集合可以消除重复，但不能维护元素顺序
print('==========3==========')
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(set(a))

## 生成器函数让我们的函数更加通用，不仅仅局限于列表处理
## 读取一个文件消除重复行
print('==========4==========')
with open(r'./somefile.txt', 'r') as f:
    for line in dedupe(f):
        print(line)















