# 通过关键字排序一个字典列表
from operator import itemgetter
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

print('==========1==========')
rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)

print('==========2==========')
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_uid)

print('==========3==========')
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)

## rows 被传递给接受一个关键字参数的 sorted() 内置函数，参数是callable类型，
## 并且从rows中接受一个单一元素，然后返回用来被排序的值
## itemgetter() 函数就是负责创建这个 callable 对象的

# operator.itemgetter() 有一个被rows中记录用来查找值的索引参数
# 可以是字典键名、整型值、任何能够传入对象的__getitem__()方法的值。
# 如果你传入多个索引参数给 itemgetter() ，它生成的 callable 对象会返回一 个包含所有元素值的元组，
## 并且 sorted() 函数会根据这个元组中元素顺序去排序。但 你想要同时在几个字段上面进行排序（比如通过姓和名来排序，也就是例子中的那样）的时候这种方法是很有用的。

## lambda 形式性能稍微低一些
print('==========4==========')
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))

## min() max() 同样适合此函数
print('==========5==========')
min_val = min(rows, key=itemgetter('uid'))
max_val = max(rows, key=itemgetter('uid'))
print(min_val)
print(max_val)










