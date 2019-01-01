# 计算当前月份的日期范围

from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date = None):
    if start_date is None:
        '''
        replace() 会创建和你传入类型相同的对象
        end_date 实际用的是下个月第一天，和Python的slice、range操作保持一致，不包含结尾
        '''
        start_date = date.today().replace(day=1)
    _, day_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=day_in_month)
    return (start_date, end_date)

a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day

## 如果能够为日期迭代创建一个同内置的 range() 函数一样的函数就好了，可以使用一个生成器容易的实现这个目标
def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step
# 使用案例
for d in date_range(datetime(2012, 9, 1), datetime(2012,10,1), timedelta(hours=6)):
    print(d)
# Python 中当日期和时间能够使用标准的数学和比较操作符
























