# 字典运算
## 在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB2': 10.75,
    'FB1': 10.75,
}

## zip() 将键和值反转过来
print('=========1===========')
prices2 = zip(prices.values(), prices.keys())
for key, value in prices2:
    print('(', key, value, ')', end=', ')
    print('')
# Outputs: ( 45.23 ACME ), ( 612.78 AAPL ), ( 205.55 IBM ), ( 37.2 HPQ ), ( 10.75 FB2 ), ( 10.75 FB1 )

print('==========2==========')
min_price = min(zip(prices.values(), prices.keys()))
print(min_price) # min_price is (10.75, 'FB1')
max_price = max(zip(prices.values(), prices.keys()))
print(max_price) # max_price is (612.78, 'AAPL')

## zip() sorted() 排序字典
print('=========3===========')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
                    (45.23, 'ACME'), (205.55, 'IBM'),
                    (612.78, 'AAPL')]

## zip() 创建的是一个只能访问一次的迭代器，第二次访问会出异常
# print('====================')
# prices_and_names = zip(prices.values(), prices.keys())
# print(min(prices_and_names)) # OK
# print(max(prices_and_names)) # ValueError: max() arg is an empty sequence

## 以字典为参数的数学运算，仅仅作用于键，而不是值
print('==========4==========')
print(min(prices))
print(max(prices))
print(min(prices.values())) # Returns 10.75
print(max(prices.values())) # Returns 612.78
## 在min()/max()中提供key函数参数来获取最小/大值对应的关键的信息
print(min(prices, key=lambda k: prices[k])) # Returns 'FB'
print(max(prices, key=lambda k: prices[k])) # Returns 'AAPL'
## 由key得到值，得再执行一次查找操作
min_value = prices[min(prices, key=lambda k: prices[k])]
print(min_value)

# zip() 通过将字典"反转"为(key, value)元素序列来解决问题，先比较value，再比较key
print('==========5==========')
prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }
print(min(zip(prices.values(), prices.keys()))) # (45.23, 'AAA')
print(max(zip(prices.values(), prices.keys()))) # (45.23, 'ZZZ')











