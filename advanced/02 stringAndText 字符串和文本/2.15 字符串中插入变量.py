# 字符串中插入变量

print('=========1=========')
s = '{name} has {n} messages'
s1 = s.format(name='Chengjs', n=37)
print(s1)

# 如果被替换的变量能在变量域中找到，可以结合使用 format_map() 和 vars()
print('=========2=========')
name = 'Guido'
n = 37
s2 = s.format_map(vars())
print(s2)

## vars() 也适用于对象实例
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n
a = Info('Chengjs', 37)
s3 = s.format_map(vars(a))
print(s3)

## format 和 format_map() 不能很好的处理变量缺失情况
# s.format(name='Guido') # Exception
## 可以另外定义一个含有__missing__()方法的字典对象
class safesub(dict):
    """防止 key 找不到"""
    def __missing__(self, key):
        return '{' + key + '}'
# 利用这个类包装输入后传递给format
print('=========3=========')
s4 = s.format_map(safesub(vars()))
print(s4)

# 如果在代码中频繁执行这些步骤，可以用变量替换步骤用一个工具函数进行封装
import sys

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))
name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}')) 






