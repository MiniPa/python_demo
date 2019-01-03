# 手动遍历迭代器

## 手动遍历一个可迭代对想中所有元素，但不用for循环
def manual_iter():
    '''手动遍历可迭代对象， StopIteration 来结束迭代'''
    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:
            pass

with open('/etc/passwd') as f:
    '''None 来指定迭代的结尾'''
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')
































