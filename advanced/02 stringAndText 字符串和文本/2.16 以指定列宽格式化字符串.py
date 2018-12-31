# 以指定列宽格式化字符串

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

# 使用 textwrap 格式化字符串
import textwrap
print('=========1=========')
print(textwrap.fill(s, 70))
print()
print(textwrap.fill(s, 30))
print()
print(textwrap.fill(s, 30, initial_indent='  '))
print()
print(textwrap.fill(s, 30, subsequent_indent='  '))
print()
## 可以用os.get_terminal_size()获取输出终端的大小
import os
print(os.get_terminal_size().columns)


























