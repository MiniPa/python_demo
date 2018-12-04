# 使用多个界定符分割string
line = 'asdf fjdk; afed, fjek,asdf, foo'

import re

print('=========1===========')
print(re.split(r'[;,\s]\s*', line))
print(line)

## 使用括号捕获分组, 保留被匹配的文本
print('=========2===========')
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

print('=========3===========')
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)
origin = ''.join(v+d for v, d in zip(values, delimiters))
print(origin)

## 不保留分割字符串到结果列表中去，仍使用括号来分组正则表达式，可用(?:...)
print('=========4===========')
fields = re.split(r'(?:,|;|\s)\s*', line)
print(fields)









