# 基本的日期和时间的转换

from datetime import timedelta

print('=========1==========')
## timedelta 表示一个时间段
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(a)
print(b)
print(c)
print(c.days)
print(c.seconds)
print(c.seconds / 3600)
print(c.total_seconds() / 3600)


from datetime import datetime

print('=========2==========')
## datetime 表示指定的日期和时间，然后用标准的数学运算来操作
a = datetime(2012, 9, 23)
print(a + timedelta(days=10))
b = datetime(2012, 12, 21)
d = b - a
print(d)
print(d.days)
now = datetime.today()
print(now)
print(now + timedelta(minutes=10))

print('=========3==========')
## datetime 会自动处理闰年
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print(a - b)
c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print((c - d).days)

print('=========4==========')
## dateutil 可以执行更加复杂的日期操作，如处理时区、模糊时间范围、节假日计算
# 许多类似的时间计算可以用 dateutil.relativedelta() 函数代替，它会在处理月份的时候填充间隙
a = datetime(2012, 9, 23)
print('a: ', a)
# a + timedelta(months=1) # TypeError: 'months' is an invalid keyword argument for this function

from dateutil.relativedelta import relativedelta

print(a + relativedelta(months=+1))

# Time between two dates
b = datetime(2012, 12, 21)
print('b: ', b)
d = b - a
print(d)

d = relativedelta(b, a)
print(d)
print(d.months)
print(d.days)













