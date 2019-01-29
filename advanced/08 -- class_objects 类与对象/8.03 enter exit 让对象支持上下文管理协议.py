# 让对象支持上下文管理协议 with 语句

# 让对象兼容 with 语句，需要实现 __enter__() 和 __exit__() 方法

print('=========1=========')
# 如下建造一个创建网络的类 连接的建立和关闭是使用 with 语句自动完成的

from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None

print('=========2=========')

from functools import partial

conn = LazyConnection(('www.python.org', 80))

with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # conn.__exit__() executes: connection closed

## 事实上，__exit__() 方法的第三个参数包含了异常类型、异常值和追溯信息 (如果有的话)
#  __exit__() 方法能自己决定怎样利用这个异常信息，或者忽略 它并返回一个 None 值
#  如果 __exit__() 返回 True ，那么异常会被清空，就好像什 么都没发生一样，with 语句后面的程序继续在正常执行

## 上面的定义中一次只能允许一个 socket 连接，如果正在使用一个 socket 的时候又重复使用 with 语句，就会产生一个异常了
#  可做如下改进

print('=========3=========')
from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()

# Example use
from functools import partial

conn = LazyConnection(('www.python.org', 80))
with conn as s1:
    pass
    with conn as s2:
        pass
# s1 and s2 are independent sockets

## contextmanager模块中有一个标准的上下文管理方案模板




























