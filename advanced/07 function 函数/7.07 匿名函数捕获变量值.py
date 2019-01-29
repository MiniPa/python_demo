# 匿名函数捕获变量值

print('=========1=========')
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
print(a(10)) # 30
print(b(10)) # 30
## lambda 表达式中的 x 是一个自由变量，在运行时绑定值，而不 是定义时就绑定，这跟函数的默认值参数定义是不同的

print('=========2=========')
## 让匿名函数在定义时就捕获到值，可以将那个参数值定义成默认参数即可
x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
print(a(10))
print(b(10))

print('=========3=========')
## 这里运行的效果是n的值为迭代的最后一个值
funcs = [lambda x: x+n for n in range(5)]
for f in funcs:
    print(f(0))

## 函数默认值参数形式，lambda 函数在定义时就能绑定到值
funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
    print(f(0))




















