# csv

import csv

print("Read CSV")
print('=========1=========')
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        print(row) # ['C', '53.08', '6/11/2007', '9:36am', '-0.25', '360900']
## 如上下标访问会引起混淆，可考虑使用命名元组

from collections import namedtuple

print('=========2=========')
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        print(row)
## 允许使用列名如 row.Symbol 和 row.Change 代替下标访问
#  只在列名是合法的 Python 的标识符的时候生效，否则需要修改下原始的列名

print('=========3=========')
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row)
        print(row['Symbol'], " - ", end='')
        print(row['Change'], " - ", end='')
## DictReader 可以使用列名访问每一行数据


print("Write CSV")
print('=========4=========')

headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [
        ('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
        ]

with open('stocks_write.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

print('=========5=========')
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
         'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
        {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
         'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
        {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
         'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
        ]
with open('stocks.csv','w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)

print('=========6=========')
## 用csv模块分割或解析CSV数据，如下写法需处理一些棘手的细节问题
with open('stocks.csv') as f:
    for line in f:
        row = line.split(',')
        print(row)
## 默认情况下，csv库可以使用 Microsoft Excel 所使用的 CSV 编码规则，这是最常见的形式，并且会带来最好的兼容性
## 如果查看csv文档，会发现还有很多方法将其应用到其他编码格式上


print('=========7=========')
# Example of reading tab-separated values
with open('stock.tsv') as f:
    f_tsv = csv.reader(f, delimiter='\t')
    for row in f_tsv:
        print(row)

print('=========8=========')
## 读取CSV并将它们转换为命名元组，需要注意对列名进行合法性认证
#  如下的CSV文件包含非法标识符的列头行，会到只创建命名元组时候产生一个 ValueError 异常而失败
# Street Address,Num-Premises,Latitude,Longitude 5412 N CLARK,10,41.980262,-87.֒668452
# 可做如下的正则表达式替换

import re

with open('stock.csv') as f:
    f_csv = csv.reader(f)
    headers = [ re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv) ]
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r)
        print(row)

print('=========9=========')
## csv 产生的数据都是字符串类型的，不会做任何其他类型的转换
#  手动进行转换
col_types = [str, float, str, str, float, int]
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Apply conversions to the row items
        row = tuple(convert(value) for convert, value in zip(col_types, row))

print('=========10=========')
## 转换字典中特定字段的例子
print('Reading as dicts with type conversion')
field_types = [ ('Price', float),
                ('Change', float),
                ('Volume', int) ]
with open('stocks.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key])) for key, conversion in field_types)
        print(row)

print('=========11=========')
## 实际中，CSV通常会有一些错误，所以必须考虑异常处理机制
## 如果对 CSV 数据进行数据分析和统计的话， 可以考虑 Pandas 包，有个 pandas.read_csv()
## 可以加载 CSV 数据到一个 DataFrame 对象中去






















