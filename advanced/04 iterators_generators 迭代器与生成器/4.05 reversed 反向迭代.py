# 反向迭代

## reversed() 仅当对象大小确定或者对象实现了 __reversed__() 的特殊方法才能生效
print('=========1===========')
a = [1, 2, 3, 4]
for x in reversed(a):
    print(a)

## Print a file backwards
print('=========2===========')
f = open('somefile.txt')
for line in reversed(list(f)):
    '''如果可迭代对象元素很多，将之转换为一个列表需消耗大量的内存'''
    print(line)

## 在类上实现反迭代方法 __reversed__()
class Countdown:

    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while  n <= self.start:
            yield n
            n += 1

print('=========3===========')
for rr in reversed(Countdown(5)):
    print(rr)

print('=========4===========')
for rr in Countdown(5):
    print(rr)













































