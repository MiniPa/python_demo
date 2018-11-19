# 构造一个字典是另一个字典的子集
## 字典推导
print('==========1==========')
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)

## dict() 通过创建一个元组序列传递给dict()，函数实现字典推导同样的功能，但慢一倍，而且不直观
p1 = dict((key, value) for key, value in prices.items() if value > 200)
p2 = { key:prices[key] for key in prices.keys() & tech_names }









