# 四舍五入

print('=========1===========')
print(round(1.23, 1))
print(round(1.25361,3))
print(round(1627731, -3))

## 一个值正好在两个边界中间的时候，round返回离他最近的偶数
print(round(1.5))
print(round(2.5))

## 舍入和格式化输出不同，仅仅输出一定宽度的数，格式化时候指定精度即可
print('=========2===========')
x = 1.23456
print(format(x, '0.2f'))
print('value is {:0.3f}'.format(x))

## 不要舍入浮点值来"修正"表面上看起来正确的问题
a = 2.1
b = 4.2
c = a + b
print(c)
c = round(c, 2) # "Fix" result (???)
print(c)








