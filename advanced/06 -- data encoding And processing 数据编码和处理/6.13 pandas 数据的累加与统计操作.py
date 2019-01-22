# 处理一个很大的数据集并需要计算数据总和或其他统计量
## pandas 任何涉及到统计、时间序列以及其他相关技术的数据分析问题
## data: 老鼠和啮齿类动物数据库 https://data.cityofchicago.org/Service-Requests/311-Service-Requests-Rodent-Baiting/97t6-zrhs

import pandas

rats = pandas.read_csv('rats.csv', skip_footer=1)
print(rats) # <class 'pandas.core.frame.DataFrame'>

# Investigate range of values for a certain field
print(rats['Current Activity'].unique())
# array([nan, Dispatch Crew, Request Sanitation Inspector], dtype=object)

# Filter the data
crew_dispatched = rats[rats['Current Activity'] == 'Dispatch Crew']
print(len(crew_dispatched))

# Find 10 most rat-infested ZIP codes in Chicago
print(crew_dispatched['ZIP Code'].value_counts()[:10])

# Group by completion date
dates = crew_dispatched.groupby('Completion Date')
# <pandas.core.groupby.DataFrameGroupBy object at 0x10d0a2a10>
print(len(dates))

# Determine counts on each day
date_counts = dates.size()
date_counts[0:10]

# Sort the counts
date_counts.sort()
date_counts[-10:]





































