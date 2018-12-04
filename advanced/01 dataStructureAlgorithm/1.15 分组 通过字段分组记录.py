# 分组 通过某个字段将字段进行分组
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

## grouby() 扫描整个序列并查找连续相同的值(根据指定key函数返回值相同)的元素序列
##  在每次迭代时候，返回一个值和一个迭代器对象，可生成元素值全等于上面那个值的组中所有对象

## note: groupby() 仅仅检查连续元素，需要事先根据属性排序完成
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
for r in rows_by_date['07/01/2012']:
    print(r)









