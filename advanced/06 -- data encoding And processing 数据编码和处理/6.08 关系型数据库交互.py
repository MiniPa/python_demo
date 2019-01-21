# 关系型数据库交互

## Python 中表示多行数据的标准方式是一个由元组构成的序列
stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),
]

## 依据 PEP249, 这种形式提供数据，很容易和Python标准数据库API进行交互
#  所有数据库上的操作通过 SQL 来查询语句完成

import sqlite3

# 1.连接数据库
db = sqlite3.connect('database.db')
# 2.创建一个游标, 并可以执行SQL查询语句
c = db.cursor()
c.execute('create table portfolio (symbol text, shares integer, pricereal)')
db.commit()

c.executemany('insert into portfolio values (?,?,?)', stocks)
db.commit()

for row in db.execute('select * from portfolio'):
    print(row)

min_price = 100
for row in db.execute('select * from portfolio where price >= ?',(min_price,)):
    print(row)































