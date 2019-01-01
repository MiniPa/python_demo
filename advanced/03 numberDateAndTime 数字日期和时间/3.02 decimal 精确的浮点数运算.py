# 精确的浮点数运算

## 浮点数不能精确的表示10进制数
# 错误原因是底层CPU和IEEE 754标准通过自己的单位去执行算术时的特征
# Python 浮点数据类型使用底层表示存储数据，所以没办法避免这样的误差
a = 4.2
b = 2.1
print(a + b)

# decimal 处理金融数据
print('=========1===========')
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)
print((a + b) == Decimal('6.3'))

## decimal 允许控制计算的每一方面，包括数字位数和四舍五入运算
# 必须创建一个本地上下文并更改它的设置
# decimal 实现了 IBM 的'通用小数运算规范'
print('=========2===========')
from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)

## 数字位数
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

## 四舍五入
with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)

## 一般工作使用float是ok的，它提供了17位精度，足够，并且运算快

## 有些方法处理误差比其他方法好，如下
print('=========3===========')
nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums)) # 答案0 是错误的

# math.fsum()提供更精确的计算能力
import math
print(math.fsum(nums)) # 答案1.0




