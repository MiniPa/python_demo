# 结合时区的日期操作
## 时区应该用 pytz 模块处理，它提供了 Olson 时区数据库，它是时区信息实时上的标准
## pytz 将 datetime 创建的简单日期对象本地化

from datetime import datetime, timedelta
import pytz
from pytz import timezone

d = datetime(2012, 12, 21, 9, 30, 0)
print(d)

print('=========1==========')
## Localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

## 日期被本地化了，就可以转化为其他时区的时间
# Convert to Bangalore time
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

print('=========2==========')
## 在本地化日期上执行计算，你需要特别注意夏令时转换和其他细节
# 在 2013 年，美国标准夏令时时间开始于本地时间 3 月 13 日凌晨 2:00(在那时，时间向前跳过一小时)
# 如果你正在执行本地计算，你会得到一个错误。

d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)
later = loc_d + timedelta(minutes=30)
print(later) # 2013-03-10 02:15:00-06:00 WRONG! WRONG!

## 可以使用时区对象 normalize() 方法
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)

print('=========3==========')
## 方案：处理本地化日期的通常的策略先将所有日 期转换为 UTC 时间，并用它来执行所有的中间存储和操作。
print(loc_d)
utc_d = loc_d.astimezone(pytz.utc) # 转换为 UTC
print(utc_d)
later_utc = utc_d + timedelta(minutes=30) # 时间操作
print(later_utc.astimezone(central)) # 转换为本地化时间
# ISO 3166 国家代码作为关键字去查阅字典 pytz.country_timezones 可得到地区对应的时间区名
print(pytz.country_timezones['IN'])













