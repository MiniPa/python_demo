# 为这个函数的参数增加一些额外的信息，这样的话其他 使用者就能清楚的知道这个函数应该怎么使用

## 参数注解
## python 解释器不会对这些注解添加任何的语义，它们不会被类型检查，运行时跟 没有加注解之前的效果也没有任何差距
## 函数注解 只存储在函数的 __annotations__ 属性中
def add(x:int, y:int) -> int:
    return x + y

print(help(add))
# Help on function add in module __main__:
#     add(x: int, y: int) -> int

print(add.__annotations__)





























