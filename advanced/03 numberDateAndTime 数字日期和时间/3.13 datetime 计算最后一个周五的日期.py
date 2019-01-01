# 计算最后一个周五的日期

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 最后的周五
Desc :
"""

from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_previous_byday(dayname, start_date=None):
    '''
    1.将开始日期、目标日期映射到星期数组位置上（星期一索引为0）
    2.通过模运算计算出目标日期经过多少天才能到达开始日期
    3.用开始日期减去时间差即得到结果日期
    :param dayname:
    :param start_date:
    :return:
    '''
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

print('=========1==========')
print(datetime.today())  # For reference
print(get_previous_byday('Monday'))
print(get_previous_byday('Tuesday'))  # Previous week, not today
print(get_previous_byday('Friday'))
print(get_previous_byday('Sunday', datetime(2012, 12, 21)))


print('=========2==========')
## 大量运算最好安装第三方包 python-dateutil 来代替
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

d = datetime.now()
print(d)

print(d + relativedelta(weekday=FR))  # Next Friday
print(d + relativedelta(weekday=FR(-1)))  # Last Friday












