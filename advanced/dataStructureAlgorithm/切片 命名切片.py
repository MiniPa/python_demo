# 硬编码切片下标非常不合适
###### 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])

## 更改为命名切片,代码更加清晰可读
## slice() 函数创建了一个切片对象，可以被用在任何切片允许使用的地方。
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
## 可调用切片对象 获取更多信息
a = slice(5, 50, 2)
print(a.start)
print(a.stop)
print(a.step)














