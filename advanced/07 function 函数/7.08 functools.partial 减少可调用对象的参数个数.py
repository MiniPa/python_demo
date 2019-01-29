# 减少可调用对象的参数个数
## 有一个被其他 python 代码使用的 callable 对象，可能是一个回调函数或者一个处理器，但参数太多了，导致调用出错

## functools.partial() 给一个或多个参数设置固定值，减少接下来被调用时的参数个数
def spam(a, b, c, d):
    print(a, b, c, d)

from functools import partial

print('=========1=========')
s1 = partial(spam, 1) # a = 1
s1(2, 3, 4)
s1(4, 5, 6)

print('=========2=========')
s2 = partial(spam, d=42) # d = 42
s2(1, 2, 3)
s2(4, 5, 6)

print('=========3=========')
s3 = partial(spam, 1, 2, d=42) # a = 1, b = 2, d = 42
s3(3)
s3(4)

## 让原本不兼容的代码可以一起工作
print('=========4=========')
points = [ (1, 2), (3, 4), (5, 6), (7, 8) ] # (x, y) 代表点

import math

def distance(p1, p2):
    '''计算两点之间的距离'''
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 -x1, y2 - y1)

# 以某个点为基点，根据点和点的距离来排序所有这些点
# sort() 接受一个关键字参数来自定义排序逻辑，但是它只能接受一个单个参数的函数 (distance() 很明显是不符合条件的)
# 现在我们可以通过使用 partial() 来解 决这个问题

pt = (4, 3)
points.sort(key=partial(distance,pt))
print(points)

# partial() 通常被用来微调其他库函数所使用的回调函数的参数
# 如下代码，使用 multiprocessing 来异步计算一个结果值，
# 然后这个值被 传递给一个接受一个 result 值和一个可选 logging 参数的回调函数

def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r', result)

def add(x, y):
    return x + y

if __name__ == '__main__':
    import logging
    from multiprocessing import Pool
    from functools import partial

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')

    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()

## 当给 apply_async() 提供回调函数时，通过使用 partial() 传递额外的 logging 参数
#  而 multiprocessing 对这些一无所知，仅仅使用单个值来调用回调函数

## 简单的 echo 服务器
from socketserver import StreamRequestHandler, TCPServer

class EchoHandler(StreamRequestHandler):
    def handle(self):
        for line in self.rfile:
            self.wfile.write(b'GOT:' + line)

serv = TCPServer(('', 15000), EchoHandler)
serv.serve_forever()

# 如果你想给 EchoHandler 增加一个可以接受其他配置选项的 __init__ 方法
class EchoHandler(StreamRequestHandler):
    # ack is added keyword-only argument. *args, **kwargs are
    # any normal parameters supplied (which are passed on)

    def __init__(self, *args, ack, **kwargs):
        ''' 申明 ack为一个强制关键字参数 '''
        self.ack = ack
        super().__init__(*args, **kwargs)

    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)
# 如此修改后，不需要显式地在 TCPServer 类中添加前缀了。但是你再次运 行程序后会报类似下面的错误
# Exception happened during processing of request from ('127.0.0.1', 59834)
# Traceback (most recent call last):
# ...
# TypeError: __init__() missing 1 required keyword-only argument: 'ack'

## 使用 partial() 就能很轻松的解决——给它传递 ack 参数的值来初始化即可解决这个错误
from functools import partial
serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVED:'))
serv.serve_forever()

## __init__() 方法中的 ack 参数声明方式看上去很有趣，其实就是 声明 ack 为一个强制关键字参数
points.sort(key=lambda p: distance(pt, p))
p.apply_async(add, (3, 4), callback=lambda result: output_result(result,log))
serv = TCPServer(
    ('', 15000),
    lambda *args, **kwargs: EchoHandler(*args, ack=b'RECEIVED:', **kwargs)
)

## partial() 能实现的效果，用 lambda 也能实现，如前面的案例可以用如下表达式
points.sort(key=lambda p: distance(pt, p))
p.apply_async(add, (3, 4), callback=lambda result: output_result(result,log))
serv = TCPServer(('', 15000), lambda *args, **kwargs: EchoHandler(*args, ack=b'RECEIVED:', **kwargs))


























































