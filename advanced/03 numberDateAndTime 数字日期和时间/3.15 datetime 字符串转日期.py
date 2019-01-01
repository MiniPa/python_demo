# 字符串转日期

from datetime import datetime

print('=========1==========')
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d') # %Y - 4位数年份 %m - 两位数月份
z = datetime.now()
diff = z - y
print(diff)

print('=========2==========')
print('z: ', z) # z:  2019-01-01 20:40:48.534711
nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z) # Tuesday January 01, 2019

## strftime() 性能非常不好，它使用纯Python实现，并且必须处理所有系统本地设置
#  可以自己实现一套方案来获取更好的性能

from datetime import datetime
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))
## 这个方案比 datetime.strftime快7倍






















