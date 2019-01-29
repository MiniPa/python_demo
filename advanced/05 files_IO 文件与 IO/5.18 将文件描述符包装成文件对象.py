# 有一个对应于操作系统上一个已打开的 I/O 通道 (比如文件、管道、套接字等) 的整型文件描述符
# 将它包装成一个更高层的 Python 文件对象

# 一个文件描述符和一个打开的普通文件是不一样的
# 文件描述符仅仅是一个由操作系统指定的整数, 用来指代某个系统的 I/O 通道

# 如果你碰巧有这么一个文件描述符，你可以通过使用 open() 函数来将其包装为一个 Python 的文件对象
# 你仅仅只需要使用这个整数值的文件描述符作为第一个参数来代替文件名即可

# Open a low-level file descriptor

import os

fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)

# Turn into a proper file
f = open(fd, 'wt')
f.write('hello world\n')
f.close()

# 当高层的文件对象被关闭或者破坏的时候，底层的文件描述符也会被关闭
# Create a file object, but don't close underlying fd when done
f = open(fd, 'wt', closefd=False)

## 在 Unix 系统中，这种包装文件描述符的技术可以很方便的将一个类文件接口作用 于一个以不同方式打开的 I/O 通道上，如管道、套接字等。
from socket import socket, AF_INET, SOCK_STREAM

def echo_client(client_sock, addr):
    print('Got connection from', addr)

    # Make text-mode file wrappers for socket reading/writing
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1', closefd=False)

    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1', closefd=False)

    # Echo lines back to the client using file I/O for line in client_in:
    line = 'line'
    client_out.write(line)
    client_out.flush()

    client_sock.close()

def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)

## 创建一个文件对象，允许你输出二进制数据到标准输出
import sys

# Create a binary-mode file for stdout
# open() 将一个文件描述符包装成正常的文件对象
# 但并不是所有的文件模式都被支持,某些类型的文件描述符可能会有副作用,特别是涉及到错误的处理、文件结尾条件等等的时候
bstdout = open(sys.stdout.fileno(), 'wb', closefd=False)
bstdout.write(b'Hello World\n')
bstdout.flush()









































