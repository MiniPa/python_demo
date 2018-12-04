# 删除字符串中不需要的字符

## strip() 去除头尾 空格 换行等， 不会对中间文本产生任何影响
print('=========1=========')
s = ' hello world \n'
print(s)
print(s.strip())
print(s.lstrip())
print(s.rstrip())

print('=========2=========')
t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))

## 处理中间的空格
print('=========3=========')
s = ' hello world \n'
print(s.replace(' ', ''))
import re
print(re.sub('\s+', ' ', s))


## 从文件中读取多行数据，将字符串strip()操作和其他迭代操作结合 == 生成器表达式
print('=========4=========')
filename = 'somefile.txt'
with open(filename) as f:
    lines = (line.strip() for line in f) # 这种方式只用创建一个生成器，非常高效
    for line in lines:
        print(line)
















